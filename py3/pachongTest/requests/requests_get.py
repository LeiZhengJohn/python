import requests
import json

response1 = requests.get("http://httpbin.org/get?name=john&age=22")
#print(response1.text)

data = {
    'name':'John',
    'age':22
}
response2 = requests.get("http://httpbin.org/get",params=data)
#print(response2.text)

response3 = requests.get("http://httpbin.org/get")
print(type(response3.text))
# <class 'str'>
print(response3.json())
# {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
#  'Connection': 'close', 'Host': 'httpbin.org',
#  'User-Agent': 'python-requests/2.18.4'}, 'origin': '42.244.62.222',
#  'url': 'http://httpbin.org/get'}
print(json.loads(response3.text))
print(type(response3.json()))
# <class 'dict'>

