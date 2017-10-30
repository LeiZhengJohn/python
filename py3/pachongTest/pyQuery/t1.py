# _*_ coding:utf-8 _*_
from pyquery import PyQuery as pq

html = '''
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>生信简单搜索主页</title>
		<link rel="stylesheet" type="text/css" href="mystyle.css" />
	</head>

	<body>
		<div id="container">
			<div class="header-left">
				<img src="picture/logo.png" width="320" height="51"/>
			</div>
			<div class="header-right">
				<form action="" method="post">
				  <font color="#F8FFB2">用户名：</font><input type="text" name="username" /><br>
					<font color="#F8FFB2">密码：</font><input type="password" name="password" />
				  <input type="submit" value="登录">
				</form>
			</div>
			<div class="link" class="o">
				<h2>为您推荐</h2>
				<ul id="ul1">
					<li class="li1"><a href="main.html">本站主页</a></li>
					<li><a href="interduction.html">关于本站</a></li>
					<li><a href="database.html">数据库简介</a></li>
					<li><a href="function3.html">Blast</a></li>
					<li><a href="about.html">关于我们</a></li>
				</ul>
				<h2>友情链接</h2>
				<ul class="ul2">
					<li><a href="http://www.ddbj.nig.ac.jp" target="_blank"><img src="picture/DDBJ_logo.png" height="37" width="100" alt="DDBJ数据库"></a></li>
					<li><a href="http://www.ebi.ac.uk/embl.html" target="_blank"><img src="picture/EMBL_logo.png" height="37" width="100" alt="EMBL数据库"></a></li>
					<li><a href="http://www.ncbi.nlm.nih.gov" target="_blank"><img src="picture/NCBI_logo.jpg" height="37" width="100" alt="NCBI数据库"></a></li>
					<li><a href="http://www.rcsb.org" target="_blank"><img src="picture/rcsb_logo.png" height="37" width="100" alt="PDB数据库"></a></li>
				</ul>
			</div>
			<div id="content">
				<form action="">
					<select name="website" id="website">
						<option id="ncbi">NCBI</option>
					</select>
					<select name="database" id="database">
						<option id="gene">Gene</option>
					</select>
					<input type="text" id="search" name="search">
					<input type="submit" value="搜索">
				</form>
			</div>
			<div id="ad">通知及广告</div>
			<p name="space" value="545" class="class">&nbsp;</p>
			<div id="footer">
				Copyright
			</div>
		</div>
'''

doc = pq(html)
print(doc('li'))

#doc1 = pq(url='http://www.baidu.com')
#print(doc1('head'))

doc2 = pq(filename='main.html')
print(doc2('li'))

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(doc('#container .link .li1'))
print(type(doc('#container .link .li1')))
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

items = doc('.ul2')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
lis1 = items.children()
print(lis1)
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

lis2 = doc('li').items()
print(type(lis2))
for li in lis2:
    print(type(li))
    print(li)