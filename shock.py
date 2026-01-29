import requests
import os

username = os.environ['SECRET_PISHOCK_USERNAME']
api_key = os.environ['SECRET_PISHOCK_API_KEY']
share_code = os.environ['SECRET_PISHOCK_SHARE_CODE']
name = os.environ['SECRET_PISHOCK_NAME']

url = 'https://do.pishock.com/api/apioperate'

def make_request(operation, **kwargs):
    json = {"Username":username,
            "Name":name,
            "Code":share_code,
            "Apikey":api_key}
    if operation == 'shock':
        json['Op'] = 0
    elif operation == 'vibrate':
        json['Op'] = 1
    elif operation == 'beep':
        json['Op'] = 2
    else:
        print('Invalid operation', operation)
        return -1
    json.update(kwargs)
    r = requests.post(url, json=json)
    if r.status_code == 200:
        return 0
    else:
        return r

def shock(duration=1, intensity=10):
    return make_request('shock', duration=str(int(duration)), intensity=str(int(intensity)))

def vibrate(duration=1, intensity=69):
    return make_request('vibrate', duration=str(int(duration)), intensity=str(int(intensity)))

def beep(duration=1):
    return make_request('beep', duration=str(int(duration)))

