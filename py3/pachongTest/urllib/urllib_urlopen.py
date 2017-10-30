from urllib import request
from urllib import parse
from urllib import error
import socket

response1 = request.urlopen('http://www.baidu.com')
#print(response1.read().decode('utf-8'))

data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
response2 = request.urlopen('http://httpbin.org/post',data=data)
#print(response2.read())

response3 = request.urlopen('http://httpbin.org/get',timeout=1)
#print(response3.read())

try:
    response4 = request.urlopen('http://httpbin.org/get',timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("Time out!")