#!python

def call(token='', hostname='endid.app'):
    try:
        import http.client as httplib # Python 3
    except:
        import httplib # Python 2.7

    conn = httplib.HTTPSConnection(hostname)
    conn.request('POST', '/api', token, {"content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
    data = response.read()
    
    print(data)

def cmd():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', action='store', default='',
                    dest='token',
                    help='Endid token from the Slack channel to call')

    results = parser.parse_args()

    call(token=results.token)

if __name__ == "__main__":
    cmd()
