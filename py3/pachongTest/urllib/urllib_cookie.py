from http import cookiejar
from urllib import request

cookie1 = cookiejar.CookieJar()
hander1 = request.HTTPCookieProcessor(cookie1)
opener1 = request.build_opener(hander1)
response1 = opener1.open('http://www.baidu.com')
for item in cookie1:
    print(item.name+'='+item.value)

filename2 = 'cookie2.txt'
cookie2 = cookiejar.MozillaCookieJar(filename2)
hander2 = request.HTTPCookieProcessor(cookie2)
opener2 = request.build_opener(hander2)
response2 = opener2.open('http://www.baidu.com')
cookie2.save(ignore_discard=True,ignore_expires=True)

filename3 = 'cookie3.txt'
cookie3 = cookiejar.LWPCookieJar(filename3)
hander3 = request.HTTPCookieProcessor(cookie3)
opener3 = request.build_opener(hander3)
response3 = opener3.open('http://www.baidu.com')
cookie3.save(ignore_discard=True,ignore_expires=True)

cookie4 = cookiejar.LWPCookieJar()
cookie4.load('cookie3.txt',ignore_discard=True,ignore_expires=True)
hander4 = request.HTTPCookieProcessor(cookie4)
opener4 = request.build_opener(hander4)
response4 = opener4.open('http://www.baidu.com')
#print(response4.read().decode('utf-8'))