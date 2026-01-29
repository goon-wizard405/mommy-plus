import requests
from sys import argv


ip = '192.168.0.84'
if __name__ == '__main__':
    if len(argv) >= 2:
        ip = argv[1]

ssl = False
if ssl:
    ip = ip.replace('.', '-')
    ip += '.lovense.club'
    port = '30010'
    proto = 'https://'
else:
    port = '20010'
    proto = 'http://'
url = proto + ip + ':' + port + '/command'

commands = ['GetToys', 'GetToyName', 'Function', 'Pattern', 'Preset']

actions = {'vibrate':   range(20+1),
           'rotate':    range(20+1),
           'pump':      range(3+1),
           'thrusting': range(20+1),
           'fingering': range(20+1),
           'suction':   range(20+1),
           'depth':     range(3+1),
           'stroke':    range(100+1),
           'oscillate': range(20+1),
           'all':       range(20+1)}

presets = ['pulse', 'wave', 'fireworks', 'earthquake']

errors = {500: 'server not running',
          400: 'invalid command',
          401: 'toy not found',
          402: 'toy not connected',
          403: 'command not supported',
          404: 'invalid parameter',
          506: 'server error'}

debug = False

def send_request(json, verbose=debug):
    r = requests.post(url, json=json)
    if verbose:
        print(r.json())
    code = r.json()['code']
    if code == 200:
        return
    if verbose:
        print('Request', json, 'returned with error code',
              code, ':', errors[code])
    return False

def function(time, power, action, verbose=debug, **kwargs):
    if action not in actions:
        if verbose:
            print('Action', action, 'not valid')
        return False
    if power not in actions[action]:
        if verbose:
            print('Power level', power, 'not valid for action', action)
        return False
    json = {'command':'function',
            'action':action+':'+str(power),
            'timeSec':time,
            'apiVer':1}
    json.update(kwargs)
    return send_request(json, verbose=verbose)

def vibe(time=1, power=5):
    return function(time, power, 'vibrate')

def pattern(strength_array, time=2, speed=200, function='v', verbose=debug, **kwargs):
    json = {'command':'Pattern',
            'rule':'V:1;F:'+function+';S:'+str(speed)+'#',
            'strength':';'.join([str(i) for i in strength_array]),
            'timeSec':time,
            'apiVer':2}
    json.update(kwargs)
    return send_request(json, verbose=verbose)

def preset(name, time, verbose=debug, **kwargs):
    if name not in presets:
        if verbose:
            print('Present', name, 'does not exist')
        return False
    json = {'command':'Preset',
            'name':name,
            'timeSec':time,
            'apiVer':1}
    json.update(kwargs)
    return send_request(json, verbose=verbose)

def stop(verbose=debug, **kwargs):
    json = {'command':'Function',
            'action':'all:0',
            'timeSec':1,
            'stopPrevious':1,
            'apiVer':1}
    json.update(kwargs)
    return send_request(json, verbose=verbose)

