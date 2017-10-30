import requests
import urllib3

# 文件上传
files = {
    'file':open('favicon.ico','rb')
}
response1 = requests.post("http://httpbin.org/post",files = files)
print(response1.text)

# 获取cookie
response2 = requests.get('https://www.baidu.com')
print(response2.cookies)
for key,value in response2.cookies.items():
    print(key + '=' + value)

# 会话维持
requests.get("http://httpbin.org/cookies/set/number/123456789")
response3 = requests.get("http://httpbin.org/cookies")
print(response3.text)

s = requests.session()
s.get("http://httpbin.org/cookies/set/number/123456789")
response4 = s.get("http://httpbin.org/cookies")
print(response4.text)

# 证书验证
urllib3.disable_warnings()
response5 = requests.get("https://www.12306.cn",verify=False)
print(response5.status_code)
#response = requests.get("https://www.12306.cn",cert=("/p/server.crt","/p/key"))

# 代理设置
proxies1 = {
    'http':"http://127.0.0.1:9743",
    'https':"https://127.0.0.1:9743"
}
response6 = requests.get("https://www.taobao.com",proxies=proxies1)
print(response6.status_code)
proxies2 = {
    'http':"http://user.password@127.0.0.1:9743/",
    'https':"https://user.password@127.0.0.1:9743/"
}
response7 = requests.get("https://www.taobao.com",proxies=proxies2)
print(response7.status_code)
#pip3 install 'requests[socks]'
proxies3 = {
    'http':"socks5://127.0.0.1:9742",
    'https':"socks5://127.0.0.1:9742"
}
response8 = requests.get("https://www.taobao.com",proxies=proxies3)
print(response8.status_code)

