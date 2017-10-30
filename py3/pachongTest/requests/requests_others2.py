import requests
from requests.auth import HTTPBasicAuth

# 认证设置
response1 = requests.get("http://120.27.34.24:9001",auth=HTTPBasicAuth('user','123'))
print(response1.status_code)

# 超时设置
try:
    response1 = requests.get("http://httpbin.org/get",timeout=0.2)
    print(response1.status_code)
except requests.ReadTimeout:
    print('Time out')


