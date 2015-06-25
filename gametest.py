# -- coding: utf-8 --
import sys
import os
import urllib
#import urllib2
import json
from datetime import datetime
 
from django.conf import settings
from django.utils.formats import localize
 
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'wordgame.settings'
 
#from rbt.models import Tune
from wordgame.models import*
from urllib import request

API_URL = 'http://127.0.0.1:8000'

def http_request(params, api):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = ''
    for k in params.keys():
        data += '&%s=%s' % (k, params[k])
    data = data[1:]
    print(data)
    try:
        req = request.Request(API_URL + api, data.encode(), headers)
        f = request.urlopen(req, timeout=10)
        response = f.read()
        f.close()
        return json.loads(response.decode())
    except Exception as e:
        print(e)
        return None
 
if __name__ == '__main__':
    print('0-gamer1 register, 1-game2 register, 2-gamer1 create game, 3-gamer2 create game,'
          ' 4-gamer1 turn, 5-gamer2 turn Q-quit')

    gamer1_id, gamer2_id = None, None
    vocabulary = None
    while True:
        c = input()
        if c in ['q', 'Q']:
            break

        if c == '0':
            params = {
                'name': 'player1',
                'serial': '12345',
                'android_reg_id': '111'
            }
            api = '/api/0.0.1/user/new/'
            val = http_request(params, api)
            print(val)
            #gamer1_id = val['gamer_id']

        elif c == '1':
            params = {
                'name': 'player2',
                'serial': '67890',
                'android_reg_id': '222'
            }
            api = '/api/0.0.1/user/new/'
            val = http_request(params, api)
            print(val)
            #gamer2_id = val['gamer_id']

        elif c == '2':
            params = {
                'gamer_id': gamer1_id,
                'game_id': None
            }
            api = '/api/0.0.1/game/new/'
            val = http_request(params, api)
            print(val)
            vocabulary = val['vocabulary']

        elif c == '3':
            params = {
                'gamer_id': gamer2_id,
                'game_id': None
            }
            api = '/api/0.0.1/game/new/'
            val = http_request(params, api)
            print(val)
            vocabulary = val['vocabulary']

        elif c == '4':
            word = input('gamer1 enter a coords:')
            coords = word.split(',')
            s = ''
            for c in coords:
                s += '&coords=%s' % c
            params = {

                'coords': s[1:]
            }
            #if not word.upper() in vocabulary:
            #    print('% not found in vocabulary')
            #    continue



    """
    tunes = Tune.objects.filter(
        provider__id=1,
        is_funbroker=True,
        submitted=True,
        verified=False
    )

    for tune in tunes:
        tune.log += u'%s: %s\n' % (localize(datetime.now()), u'Проверяется...')
 
        params = {
            'content_package_name': tune.content_package_name,
            'media_item_id': tune.code,
        }
        verify_url = settings.FUNBROKER_API_URL + 'verify'
        response = urllib2.urlopen(verify_url, urllib.urlencode(params)).read()
        result = json.loads(response)
 
        if result['status'] == 'success':
            if result['result'] == 'ready':
                tune.verified = True
                tune.verified_date = datetime.now()
                tune.log += u'%s: %s\n' % (localize(datetime.now()), u'Проверена. Можно приобрести')
            elif result['result'] == 'not-verified':
                tune.log += u'%s: %s\n' % (localize(datetime.now()), u'Еще не готово')
            elif result['result'] == 'error':
                tune.log += u'%s: %s\n' % (localize(datetime.now()),
                                           u'Мелодия не одобрена. Пожалуйста, проверьте ошибки загрузки')
        else:
            tune.log += u'%s: %s\n' % (localize(datetime.now()), u'Ошибка при проверке!')
 
        tune.save()
    """