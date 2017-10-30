import requests

response1 = requests.get("https://www.zhihu.com/explore")
print(response1.text)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}
response2 = requests.get("https://www.zhihu.com/explore",headers=headers)
print(response2.text)