from urllib import request

response = request.urlopen("http://www.python.org")
print(type(response))
# <class 'http.client.HTTPResponse'>
print(response.status)
# 200
print(response.getheaders())
# [('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'),
# ('X-Frame-Options', 'SAMEORIGIN'), ('x-xss-protection', '1; mode=block'),
# ('X-Clacks-Overhead', 'GNU Terry Pratchett'), ('Content-Length', '49062'),
# ('Accept-Ranges', 'bytes'), ('Date', 'Tue, 17 Oct 2017 15:34:44 GMT'),
# ('Via', '1.1 varnish'), ('Age', '1826'), ('Connection', 'close'),
# ('X-Served-By', 'cache-hkg17928-HKG'), ('X-Cache', 'HIT'),
# ('X-Cache-Hits', '5'), ('X-Timer', 'S1508254484.119037,VS0,VE0'),
# ('Vary', 'Cookie'),
# ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')]
print(response.getheader('Server'))
# nginx