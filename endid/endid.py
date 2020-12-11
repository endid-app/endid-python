#!python

def call(token='', message='', hostname='endid.app', path='/api'):
    try:
        import http.client as httplib # Python 3
    except:
        import httplib # Python 2.7

    if token == '':
        print('Please provide a token')

    conn = httplib.HTTPSConnection(hostname)

    try:
        from urllib.parse import urlencode # Python 3
    except:
        from urllib import urlencode # Python 2.7

    params = {'token': token}

    if message != '':
        params['message'] = message

    body = urlencode(params)

    conn.request('POST', path, token, {"content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
    data = response.read()
    
    print(data)

def cmd():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', action='store', default='',
                    dest='token',
                    help='Endid token from the Slack channel to call')

    parser.add_argument('-m', action='store', default='',
                    dest='message',
                    help='Message to display (optional)')

    results = parser.parse_args()

    call(token=results.token, message=results.message)

if __name__ == "__main__":
    cmd()
