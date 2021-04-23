#!python

PYVER = 3
escape_str = None
unescape_str = None

try:
    FileNotFoundError # Python 3
    def escape_str_py3(s):
        return s.encode('unicode_escape').decode("utf-8")
    def unescape_str_py3(s):
        return s.encode("utf-8").decode('unicode_escape')
    escape_str = escape_str_py3
    unescape_str = unescape_str_py3
except NameError:
    FileNotFoundError = EnvironmentError # Python 2
    def escape_str_py2(s):
        return s.encode('string_escape')
    def unescape_str_py2(s):
        return s.decode('string_escape')
    escape_str = escape_str_py2
    unescape_str = unescape_str_py2
    PYVER = 2

import os
prefs_filepath = os.path.expanduser("~/.endid")

def read_prefs():
    import re
    prefs = {}
    try:
        with open(prefs_filepath, 'rt') as f:
            contents = f.read()
            for m in re.finditer('^\s*(token|message)\s*\:\s*(.*?)\s*$', contents, re.MULTILINE):
                prefs[m.group(1)] = unescape_str(m.group(2))
                
    except FileNotFoundError:
        pass

    return prefs

def write_prefs(prefs):
    try:
        with open(prefs_filepath, 'wt') as f:
            f.writelines(["".join([k,': ',escape_str(v),"\n"]) for k,v in prefs.items()])
    except FileNotFoundError as e:
        print('Unable to write prefs to file '+prefs_filepath+': '+str(e))

def call(token='', message='', name='', status='', writeprefs=True, readprefs=True, printoutput=False):

    hostname = os.environ.get('ENDID_API_HOSTNAME', 'api.endid.app')

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
            if printoutput:
                print('Please provide a token')
            return 'Please provide a token'
        elif printoutput:
            print('Using token '+token)
            

    if message == '' and token == prefs.get('token', ''):
        message = prefs.get('message', '')

    if name == '' and token == prefs.get('token', ''):
        name = prefs.get('name', '')

    conn = httplib.HTTPSConnection(hostname)

    try:
        from urllib.parse import urlencode # Python 3
    except:
        from urllib import urlencode # Python 2.7

    params = {'token': token}

    if message != '':
        params['message'] = message

    if status != '':
        params['status'] = status

    if name != '':
        params['name'] = name

    body = urlencode(params)

    conn.request('POST', '/', body, {"content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
    data = response.read()

    data = data.decode("utf-8")

    if writeprefs:
        write_prefs(params)
    
    if printoutput:
        print('Response: '+data)

    if data[:5] == 'Sorry':
        raise Exception('Endid returned an error: '+data)

    return data

def cli():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', action='store', default='',
                    dest='token',
                    help='Endid token from the Slack channel to call (optional if saved in prefs file already)')

    parser.add_argument('-m', action='store', default='',
                    dest='message',
                    help='Message to display (optional)')

    parser.add_argument('-n', action='store', default='',
                    dest='name',
                    help='Name to identify the event source (optional)')

    parser.add_argument('-s', action='store', default='',
                    dest='status',
                    help='Status of your event OK | WARN | FAIL (optional)')

    parser.add_argument('-w', action='store_false',
                    dest='writeprefs',
                    help='Do NOT write this session parameters to prefs file ~/.endid')

    parser.add_argument('-r', action='store_false',
                    dest='readprefs',
                    help='Do NOT read omitted params from prefs file ~/.endid')


    results = parser.parse_args()

    call(token=results.token, message=results.message, name=results.name, status=results.status, writeprefs=results.writeprefs, readprefs=results.readprefs, printoutput=True)

if __name__ == "__main__":
    cli()
