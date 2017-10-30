import requests

data = {'name':'Jhon',"age":22}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}
response = requests.post("http://httpbin.org/post",data=data,headers=headers)
print(response.text)
print(response.json())