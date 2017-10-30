import requests

response = requests.get('http://www.baidu.com/')
print(type(response))
# <class 'requests.models.Response'>
print(response.status_code)
# 200
print(type(response.text))
# <class 'str'>
print(response.text)
print(response.cookies)
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>