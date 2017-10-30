from urllib import request,error
import socket

try:
    response1 = request.urlopen('http://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)

try:
    response2 = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print("请求成功！")

try:
    response3 = request.urlopen("http://www.baidu.com",timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("请求超时！")
