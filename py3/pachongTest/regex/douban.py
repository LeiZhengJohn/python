import requests
import re

content = requests.get("https://book.douban.com/").text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?abstract">(.*?)</p>.*?</li>',re.S)
results = re.findall(pattern,content)
for result in results:
    url,title,author,date,publisher,abstract = result
    author = re.sub('\s','',author)
    date = date.strip()
    publisher = publisher.strip()
    abstract  = re.sub('\s','',abstract)
    print(title,url,author,date,publisher,abstract)