import json

from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from wordgame.models import Gamer, Game, Turn
from wordgame.utils.push import send_gcm


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def json_success_response(data={}):
    data['result'] = 'success'
    return json_response(data)


def json_error_response(message='Error'):
    data = {
        'result': 'error',
        'message': message,
    }
    return json_response(data)


class TestPushView(View):
    def post(self, request):
        android_reg_id = request.POST.get('android_reg_id')

        if android_reg_id is None:
            return json_error_response('android_reg_id is required')

        result = send_gcm(android_reg_id, {
            'test-data': 'Umid Qovun JPRQ',
        })

        if result:
            return json_success_response({
                'message': 'Push is sent to %s' % android_reg_id,
            })
        else:
            return json_error_response('Push is not sent to %s' % android_reg_id)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TestPushView, self).dispatch(*args, **kwargs)


class NewUserView(View):
    def post(self, request):
        user_name = request.POST.get('name')
        serial = request.POST.get('serial')
        android_reg_id = request.POST.get('android_reg_id')

        if not android_reg_id or not serial:
            return json_error_response('android_reg_id and serial number are required')

        is_new = False

        try:
            gamer = Gamer.objects.get(serial=serial)
        except Gamer.DoesNotExist:
            gamer = Gamer(name=user_name, serial=serial, android_reg_id=android_reg_id)
            gamer.save()
            is_new = True

        return json_success_response({
            'gamer_id': gamer.object_id,
            'is_new': is_new,
        })

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(NewUserView, self).dispatch(*args, **kwargs)


class UserActiveGamesView(View):
    def post(self, request):
        gamer_id = request.POST.get('gamer_id')

        try:
            gamer = Gamer.objects.get(object_id=gamer_id)
        except Gamer.DoesNotExist:
            return json_error_response('Gamer doesn\'t exist')


        games = gamer.open_games()
        if len(games) < 1:
            return json_error_response('Games doesn\'t exist')

        result = {
            'games': [],
        }

        for game in games:
            current_gamer_number = game.is_gamers_game(gamer_id)
            if current_gamer_number is False:
                continue
            opponent_score = game.opponent_score
            owner_score = game.owner_score
            is_owner = True
            game_status = game.game_status(game.owner)

            if current_gamer_number == 2:
                owner_score = game.opponent_score
                opponent_score = game.owner_score
                is_owner = False
                game_status = game.game_status(game.opponent)

            g = {
                'is_owner': is_owner,
                'is_my_turn': game.turning_gamer() == gamer,
                'game_id': game.object_id,
                'letters': game.letters.split(','),
                'board_status': game_status,
                'owner_score': owner_score,
                'opponent_score': opponent_score
            }

            turn = game.last_turn()
            if turn:
                g['coords'] = turn.coords.split(',')
                g['word'] = turn.word.split(',')

            result['games'].append(g)

        return json_success_response(result)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserActiveGamesView, self).dispatch(*args, **kwargs)


class UserSurrendGameView(View):
    def post(self, request):
        gamer_id = request.POST.get('gamer_id')
        game_id = request.POST.get('game_id')
        try:
            gamer = Gamer.objects.get(object_id=gamer_id)
        except Gamer.DoesNotExist:
            return json_error_response('Gamer doesn\'t exist')

        try:
            game = Game.objects.get(object_id=game_id)
        except Game.DoesNotExist:
            return json_error_response('Game doesn\'t exist')

        current_gamer_number = game.is_gamers_game(gamer_id)
        if current_gamer_number is False:
            return json_error_response('Permission error')

        if current_gamer_number == 1:
            game.opponent_score += game.owner_score
            game.owner_score = 0
        else:
            game.owner_score += game.opponent_score
            game.opponent_score = 0

        game.deactivate()
        game.save()

        result = {
            'message': 'You lost'
        }
        return json_success_response(result)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserSurrendGameView, self).dispatch(*args, **kwargs)


class UserDeleteGamesView(View):
    def post(self, request):
        gamer_id = request.POST.get('gamer_id')
        game_id = request.POST.get('game_id')

        try:
            gamer = Gamer.objects.get(object_id=gamer_id)
        except Gamer.DoesNotExist:
            return json_error_response('Gamer doesn\'t exist')

        try:
            game = Game.objects.get(object_id=game_id)
        except Game.DoesNotExist:
            return json_error_response('Game doesn\'t exist')

        if game.owner != gamer:
            return json_error_response('Permission denied for delete')
        else:
            game.delete_game()
            game.save()
            return json_success_response({'message': 'game deleted'})

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserDeleteGamesView, self).dispatch(*args, **kwargs)


class NewGameView(View):
    def post(self, request):
        gamer_id = request.POST.get('gamer_id')
        game_id = request.POST.get('game_id')

        try:
            gamer = Gamer.objects.get(object_id=gamer_id)
        except Gamer.DoesNotExist:
            return json_error_response('Gamer doesn\'t exist')

        is_new = False
        game = None

        if game_id:
            try:
                game = Game.objects.get(object_id=game_id)
            except Game.DoesNotExist:
                pass

        if game is None:
            open_games = Game.open_games(gamer)[:1]
            if len(open_games) > 0:
                game = open_games[0]

        if game is None:
            game = Game(owner=gamer)
            game.init_game()
            game.save()
            is_new = True
        else:
            game.opponent = gamer
            game.save()

        result = {
            'is_new': is_new,
            'game_id': game.object_id,
            'letters': game.letters.split(','),
            'vocabulary': game.vocabulary.split(','),
            'is_my_turn': game.turning_gamer() == gamer,
        }

        turn = game.last_turn()
        if turn:
            result['turn'] = {
                'word': turn.word.split(','),
                'coords': turn.coords.split(','),
            }

        if is_new:
            result['board_status'] = game.game_status(game.owner)
            result['gamer'] = {
                'name': game.owner.name,
                'score': game.owner_score,
            }
            result['opponent'] = None
        else:
            result['board_status'] = game.game_status(game.opponent)
            result['gamer'] = {
                'name': game.opponent.name,
                'score': game.opponent_score,
            }

            result['opponent'] = {
                'name': game.owner.name,
                'score': game.owner_score,
            }

        return json_success_response(result)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(NewGameView, self).dispatch(*args, **kwargs)


class GameTurnView(View):
    def post(self, request):
        game_id = request.POST.get('game_id')
        gamer_id = request.POST.get('gamer_id')
        coords = request.POST.getlist('coords')

        if not coords:
            return json_error_response('coords is required')

        try:
            game = Game.objects.get(object_id=game_id)
        except Game.DoesNotExist:
            return json_error_response('Game doesn\'t exist')

        #return json_error_response(game.letters)

        current_gamer_number = game.is_gamers_game(gamer_id)
        if current_gamer_number is False:
            return json_error_response('Permission error')

        gamer = game.owner
        opponent = game.opponent
        if current_gamer_number == 2:
            gamer = game.opponent
            opponent = game.owner

        if game.turning_gamer() != gamer:
            return json_error_response('Not your turn')

        turn_coords = []
        for coord in coords:
            try:
                turn_coords.append(int(coord))
            except ValueError:
                return json_error_response('Value error: not an integer')

        game.new_turn(turn_coords, current_gamer_number == 1)

        #turn = Turn()
        #turn.game = game
        #turn.gamer = gamer
        #turn.coords = game.coords_to_status(turn_coords)
        #turn.board_status = game.board_status
        #turn.word = game.get_word(turn_coords)
        #turn.owner_score = game.owner_score
        #turn.opponent_score = game.opponent_score
        #turn.save()
        #game.turns.add(turn)
        game.turns.create(game=game,
                          gamer=gamer,
                          coords=game.coords_to_status(turn_coords),
                          board_status=game.board_status,
                          word=game.get_word(turn_coords),
                          owner_score=game.owner_score,
                          opponent_score=game.opponent_score
        )

        game.save()

        gamer_score = game.owner_score
        opponent_score = game.opponent_score
        if current_gamer_number == 2:
            gamer_score = game.opponent_score
            opponent_score = game.owner_score

        game_status = game.game_over()

        sent = opponent.send_push({
            'game_id': game.object_id,
            'coords': turn_coords,
            'board_status': game.game_status(opponent),
            'game_status': game_status,
            'gamer': {
                'score': opponent_score
            },
            'opponent': {
                'score': gamer_score,
            }

        })

        if sent:
            opponent.push_notification.create(reg_ids=opponent.android_reg_id)

        return json_success_response({
            'board_status': game.game_status(gamer),
            'game_status': game_status,
            'gamer': {
                'score': gamer_score
            },
            'opponent': {
                'score': opponent_score,
            }
        })

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GameTurnView, self).dispatch(*args, **kwargs)
