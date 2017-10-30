from urllib.parse import urlparse,urlunparse,urljoin,urlencode

result1 = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(type(result1),result1)
# <class 'urllib.parse.ParseResult'>
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
# params='user', query='id=5', fragment='comment')

result2 = urlparse("www.baidu.com/index.html;user?id=5#comment",scheme='https')
print(result2)
# ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html',
# params='user', query='id=5', fragment='comment')

result3 = urlparse("http://www.baidu.com/index.html;user?id=5#comment",scheme='https')
print(result3)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
# params='user', query='id=5', fragment='comment')

result4 = urlparse("http://www.baidu.com/index.html;user?id=5#comment",allow_fragments=False)
print(result4)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
# params='user', query='id=5#comment', fragment='')

result5 = urlparse("http://www.baidu.com/index.html#comment",allow_fragments=False)
print(result5)
# ParseResult(scheme='http', netloc='www.baidu.com',
# path='/index.html#comment', params='', query='', fragment='')

data = ['http','www.baidu.com','index.html','user','id=6','comment']
print(urlunparse(data))
# http://www.baidu.com/index.html;user?id=6#comment

print(urljoin("http://www.baidu.com","FAQ.html"))
# http://www.baidu.com/FAQ.html
print(urljoin("http://www.baidu.com","https://cuiqingcai.com/FAQ.html"))
# https://cuiqingcai.com/FAQ.html
print(urljoin("http://www.baidu.com/about.html","https://cuiqingcai.com/FAQ.html"))
# https://cuiqingcai.com/FAQ.html
print(urljoin("http://www.baidu.com/about.html","https://cuiqingcai.com/FAQ.html?question=2"))
# https://cuiqingcai.com/FAQ.html?question=2
print(urljoin("http://www.baidu.com?wd=abc","https://cuiqingcai.com/index.php"))
# https://cuiqingcai.com/index.php
print(urljoin("http://www.baidu.com","?categery=2#comment"))
# http://www.baidu.com?categery=2#comment
print(urljoin("www.baidu.com","?categery=2#comment"))
# www.baidu.com?categery=2#comment
print(urljoin("www.baidu.com#comment","?categery=2"))
# www.baidu.com?categery=2

params = {
    'name':'郑磊',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
# http://www.baidu.com?name=%E9%83%91%E7%A3%8A&age=22
