from urllib import request,parse

request1 = request.Request("https://python.org")
response1 = request.urlopen(request1)
#print(response1.read().decode('utf-8'))

url = "http://httpbin.org/post"
headers = {
    'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name' : '郑磊'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
request2 = request.Request(url=url,data=data,headers=headers,method='POST')
response2 = request.urlopen(request2)
#print(response2.read().decode('utf-8'))

request3 = request.Request(url=url,data=data,method='POST')
request3.add_header( 'User-Agent','Mozilla/5.0 (MSIE 5.5;Windows NT)')
response3 = request.urlopen(request3)
print(response3.read().decode('utf-8'))