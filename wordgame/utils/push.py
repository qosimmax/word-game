from urllib import request
import json

from django.conf import settings


def send_gcm(android_reg_id, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + settings.GCM_API_KEY
    }

    json_data = {
        'registration_ids': [android_reg_id],
        'data': data,
        #'time_to_live': timeLife
    }

    gcm_data = json.dumps(json_data)

    try:
        req = request.Request(settings.GCM_URL, gcm_data.encode(), headers)
        f = request.urlopen(req, timeout=10)
        response = f.read()
        f.close()

        if response.find(b'"failure":0') > -1:
            return True
        else:
            return False
    except Exception:
        return False