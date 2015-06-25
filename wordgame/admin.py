from django.contrib import admin
from wordgame.models import Word, Gamer, Game, Turn, PushNotification


class WordAdmin(admin.ModelAdmin):
    search_fields = ['word']


class GamerAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'letters',
        'owner',
        'opponent',
        'started',
        'finished',
    )


class TurnAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
admin.site.register(Gamer, GamerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Turn, TurnAdmin)
admin.site.register(PushNotification)