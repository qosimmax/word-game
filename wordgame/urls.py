from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from wordgame import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', 'wordgame.views.home', name='home'),

    url(r'^api/0.0.1/user/new/', views.NewUserView.as_view()),

    url(r'^api/0.0.1/game/new/', views.NewGameView.as_view()),
    url(r'^api/0.0.1/game/turn/', views.GameTurnView.as_view()),
    url(r'^api/0.0.1/game/delete/', views.UserDeleteGamesView.as_view()),

    url(r'^api/0.0.1/user/games/', views.UserActiveGamesView.as_view()),
    url(r'^api/0.0.1/user/surrend/', views.UserSurrendGameView.as_view()),
    # url(r'^api/0.0.1/user/turn/', views.game_turn),

    url(r'^api/0.0.1/test/push/', views.TestPushView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
