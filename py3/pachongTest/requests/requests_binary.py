import requests

response1 = requests.get("https://github.com/favicon.ico")
print(type(response1.text),type(response1.content))
print(response1.text)
print(response1.content)
with open('favicon.ico','wb') as file:
    file.write(response1.content)
    file.close()