import urllib.request

proxy_handler = urllib.request.ProxyHandler(
    {'http':'http://127.0.0.1',
     'https':'http://127.0.0.1:9743'}
)
opener = urllib.request.build_opener(proxy_handler)
response1 = opener.open("http://www.baidu.com")
print(response1.read())