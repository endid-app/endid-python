#!python

try:
    FileNotFoundError # Python 3
except NameError:
    FileNotFoundError = EnvironmentError # Python 2

import os
prefs_filepath = os.path.expanduser("~/.endid")

def read_prefs():
    import re
    prefs = {}
    try:
        with open(prefs_filepath, 'rt') as f:
            for l in f.readlines():
                if l.strip() != '':
                    r = re.match('^\s*([a-z]+)\s*\:\s*(.*?)\s*$', l)
                    if r:
                        prefs[r.group(1)] = r.group(2)
                    else:
                        print('Invalid prefs file '+prefs_filepath+' line: '+l)
    except FileNotFoundError:
        pass

    return prefs

def write_prefs(prefs):
    try:
        with open(prefs_filepath, 'wt') as f:
            f.writelines(["".join([k,': ',v,"\n"]) for k,v in prefs.items()])
    except FileNotFoundError as e:
        print('Unable to write prefs to file '+prefs_filepath+': '+str(e))

def call(token='', message='', hostname='api.endid.app', path='/', writeprefs=True, readprefs=True):
    try:
        import http.client as httplib # Python 3
    except:
        import httplib # Python 2.7

    prefs = {}
    if readprefs:
        prefs = read_prefs()

    if token == '':
        token = prefs.get('token', '')
        if token == '':
            print('Please provide a token')
            return 'Please provide a token'

    if message == '' and token == prefs.get('token', ''):
        message = prefs.get('message', '')


    conn = httplib.HTTPSConnection(hostname)

    try:
        from urllib.parse import urlencode # Python 3
    except:
        from urllib import urlencode # Python 2.7

    params = {'token': token}

    if message != '':
        params['message'] = message

    body = urlencode(params)

    conn.request('POST', path, body, {"content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
    data = response.read()

    if writeprefs:
        write_prefs(params)
    
    print(data)
    return data

def cli():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', action='store', default='',
                    dest='token',
                    help='Endid token from the Slack channel to call')

    parser.add_argument('-m', action='store', default='',
                    dest='message',
                    help='Message to display (optional)')

    parser.add_argument('-w', action='store_false',
                    dest='writeprefs',
                    help='Do NOT write this session parameters to prefs file ~/.endid')

    parser.add_argument('-r', action='store_false',
                    dest='readprefs',
                    help='Do NOT read omitted params from prefs file ~/.endid')


    results = parser.parse_args()

    call(token=results.token, message=results.message, writeprefs=results.writeprefs, readprefs=results.readprefs)

if __name__ == "__main__":
    cli()
