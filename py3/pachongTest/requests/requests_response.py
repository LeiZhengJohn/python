import requests

response1 = requests.get("http://www.jianshu.com")
print(type(response1.status_code),response1.status_code)
print(type(response1.headers),response1.headers)
print(type(response1.cookies),response1.cookies)
print(type(response1.url),response1.url)
print(type(response1.history),response1.history)

response2 = requests.get("http://www.jianshu.com/1.html")
exit() if not response2.status_code == requests.codes.not_found else print("404 Not Found")

