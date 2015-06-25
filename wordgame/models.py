import random

from django.db import models
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.utils import timezone
from django.conf import settings

from wordgame.utils.utilities import generate_hash_id
from wordgame.utils.push import send_gcm


ABC = [
    'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z',
    'O‘', 'G‘', 'C',
]


# New cell statuses
CELL_OWNER_BLOCKED = -2
CELL_OWNER_SELECTED = -1
CELL_FREE = 0
CELL_OPPONENT_SELECTED = 1
CELL_OPPONENT_BLOCKED = 2


class Word(models.Model):
    object_id = models.TextField(max_length=32, unique=True, null=True)

    word = models.CharField(max_length=50, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.object_id is None:
            self.object_id = generate_hash_id()

        super(Word, self).save(force_insert=force_insert, force_update=force_update, using=using,
                               update_fields=update_fields)


class Gamer(models.Model):
    object_id = models.TextField(max_length=32, unique=True, null=True)

    name = models.CharField(max_length=40, null=True)

    serial = models.CharField(max_length=200, blank=True, null=True)
    android_reg_id = models.CharField(max_length=4096, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.object_id is None:
            self.object_id = generate_hash_id()

        super(Gamer, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                update_fields=update_fields)

    def send_push(self, data):
        return send_gcm(self.android_reg_id, data)

    def games(self):
        return Game.objects.filter(Q(owner__id=self.id) | Q(opponent__id=self.id)).order_by('-started')

    def open_games(self):
        return Game.objects.filter(finished=None).filter(is_active=True)\
            .filter(Q(owner__id=self.id) | Q(opponent__id=self.id))\
            .order_by('-started')


class Game(models.Model):
    object_id = models.TextField(max_length=32, unique=True, null=True)

    owner = models.ForeignKey(to=Gamer, related_name='ownered_games')
    opponent = models.ForeignKey(to=Gamer, blank=True, null=True, related_name='joined_games')

    letters = models.CharField(max_length=100, null=True)
    vocabulary = models.TextField(null=True)

    owner_score = models.IntegerField(default=0)
    opponent_score = models.IntegerField(default=0)

    board_status = models.CommaSeparatedIntegerField(max_length=100, null=True)

    is_active = models.BooleanField(default=True)

    started = models.DateTimeField(auto_now_add=True, null=True)
    finished = models.DateTimeField(null=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.object_id

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)

    def init_game(self):
        self.board_status = ','.join(['0' for x in range(settings.LETTERS_LENGTH)])

        self.generate_letters()
        self.generate_vocabulary()

    def deactivate(self):
        self.is_active = False
        self.finished = timezone.now()

    def delete_game(self):
        self.deactivate()
        self.is_deleted = True

    def game_over(self):
        st = str(CELL_FREE) in self.board_status
        if not st:
            self.finished = timezone.now()
        return st

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.object_id is None:
            self.object_id = generate_hash_id()

        super(Game, self).save(force_insert=force_insert, force_update=force_update, using=using,
                               update_fields=update_fields)

    def generate_letters(self):
        letters = []
        for i in range(settings.LETTERS_LENGTH):
            letters.append(random.choice(ABC))

        self.letters = ','.join(letters)

    def generate_vocabulary(self):
        words = Word.objects.all()
        set_variant = set(''.join(self.letters.split(',')))

        vocabulary = []
        for w in words:
            word = w.word.upper()
            word_chars = set(word)
            if word_chars.issubset(set_variant):
                vocabulary.append(word)

        self.vocabulary = ','.join(vocabulary)

    def get_word(self, coords):
        word = ''
        for coord in coords:
            word += self.letters[coord]
        return word

    def last_turn(self):
        try:
            return self.turns.order_by('-played')[:1].get()
        except Turn.DoesNotExist:
            return None

    def is_gamers_game(self, gamer_id):
        if self.opponent is None and self.owner.object_id != gamer_id:
            return False

        if self.owner.object_id == gamer_id:
            return 1

        if self.opponent.object_id == gamer_id:
            return 2

        return False

    def turning_gamer(self):
        #if self.opponent is None:
        #    return self.owner

        game_last_turn = self.last_turn()
        if game_last_turn is None:
            return self.owner

        if game_last_turn.gamer == self.owner:
            return self.opponent
        else:
            return self.owner

    def status_to_coords(self, status=''):
        return [int(ch) for ch in status.split(',')]

    def coords_to_status(self, coords):
        return ','.join([str(coords) for coords in coords])

    def game_status(self, gamer):
        if gamer == self.owner:
            return self.status_to_coords(self.board_status)
        else:
            req_status = self.status_to_coords(self.board_status)
            for i in range(len(req_status)):
                if req_status[i] != 0:
                    req_status[i] = -req_status[i]

            return req_status

    def new_turn(self, coords, is_gamer1=True):
        status_coords = self.status_to_coords(self.board_status)

        for index in coords:
            status_value = status_coords[index]

            if status_value in [CELL_OWNER_BLOCKED, CELL_OPPONENT_BLOCKED]:
                continue

            if is_gamer1:
                if status_value == CELL_FREE or status_value == CELL_OPPONENT_SELECTED:
                    self.owner_score += 1
                    if status_value == CELL_OPPONENT_SELECTED:
                        self.opponent_score -= 1

                    status_value = CELL_OWNER_SELECTED
            else:
                if status_value == CELL_FREE or status_value == CELL_OWNER_SELECTED:
                    self.opponent_score += 1
                    if status_value == CELL_OWNER_SELECTED:
                        self.owner_score -= 1

                    status_value = CELL_OPPONENT_SELECTED

            status_coords[index] = status_value

        for index in range(len(status_coords)):
            if status_coords[index] in [CELL_OWNER_SELECTED, CELL_OWNER_BLOCKED]:
                top_value = status_coords[index - 5] if index - 5 >= 0 else -5
                left_value = status_coords[index - 1] if index - 1 >= 0 and index % 5 != 0 else -5
                right_value = status_coords[index + 1] \
                    if index + 1 < len(status_coords) and (index + 1) % 5 != 0 else -5

                bottom_value = status_coords[index + 5] if index + 5 < len(status_coords) else -5

                if top_value <= CELL_OWNER_SELECTED and left_value <= CELL_OWNER_SELECTED \
                        and right_value <= CELL_OWNER_SELECTED and bottom_value <= CELL_OWNER_SELECTED:
                    status_coords[index] = CELL_OWNER_BLOCKED
                else:
                    status_coords[index] = CELL_OWNER_SELECTED

            if status_coords[index] in [CELL_OPPONENT_SELECTED, CELL_OPPONENT_BLOCKED]:
                top_value = status_coords[index - 5] if index - 5 >= 0 else 5
                left_value = status_coords[index - 1] if index - 1 >= 0 and index % 5 != 0 else 5
                right_value = status_coords[index + 1] \
                    if index + 1 < len(status_coords) and (index + 1) % 5 != 0 else 5

                bottom_value = status_coords[index + 5] if index + 5 < len(status_coords) else 5

                if top_value >= CELL_OPPONENT_SELECTED and left_value >= CELL_OPPONENT_SELECTED \
                        and right_value >= CELL_OPPONENT_SELECTED and bottom_value >= CELL_OPPONENT_SELECTED:
                    status_coords[index] = CELL_OPPONENT_BLOCKED
                else:
                    status_coords[index] = CELL_OPPONENT_SELECTED

        self.board_status = self.coords_to_status(status_coords)

    @staticmethod
    def open_games(gamer):
        return Game.objects.filter(opponent=None).filter(is_active=True).exclude(owner__id=gamer.id).order_by('started')


class Turn(models.Model):
    object_id = models.TextField(max_length=32, unique=True, null=True)

    game = models.ForeignKey(to=Game, related_name='turns')
    gamer = models.ForeignKey(to=Gamer)

    coords = models.CommaSeparatedIntegerField(max_length=100)
    board_status = models.CommaSeparatedIntegerField(max_length=100, null=True)
    word = models.CharField(max_length=30)

    owner_score = models.IntegerField(default=0)
    opponent_score = models.IntegerField(default=0)

    played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.object_id is None:
            self.object_id = generate_hash_id()

        super(Turn, self).save(force_insert=force_insert, force_update=force_update,
                               using=using, update_fields=update_fields)


class PushNotification(models.Model):
    object_id = models.TextField(max_length=32, unique=True, null=True)

    gamers = models.ManyToManyField(to=Gamer, related_name='push_notification')

    reg_ids = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.object_id is None:
            self.object_id = generate_hash_id()

        super(PushNotification, self).save(force_insert=force_insert, force_update=force_update,
                                           using=using, update_fields=update_fields)