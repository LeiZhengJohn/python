from bs4 import BeautifulSoup

html1 = '''
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>生信简单搜索主页</title>
		<link rel="stylesheet" type="text/css" href="mystyle.css" />
	</head>

	<body>
		<div class="container">
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
			<div id="link" class="o">
				<h2>为您推荐</h2>
				<ul id="ul1">
					<li><a href="main.html">本站主页</a></li>
					<li><a href="interduction.html">关于本站</a></li>
					<li><a href="database.html">数据库简介</a></li>
					<li><a href="function3.html">Blast</a></li>
					<li><a href="about.html">关于我们</a></li>
				</ul>
				<h2>友情链接</h2>
				<ul id="ul2">
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
soup1 = BeautifulSoup(html1,'lxml')
print(type(soup1.find_all(name='ul')))
print(soup1.find_all('ul'))
print(type(soup1.find_all('ul')[0]))
for ul in soup1.find_all('ul'):
    print(ul.find_all('li'))
print(soup1.find_all(attrs={'id':'ad'}))
print(soup1.find_all(attrs={'class':'class'}))
print(soup1.find_all(id='ad'))
print(soup1.find_all(class_='class'))
print(soup1.find_all(text='通知及广告'))
# find 返回查找到的第一个标签
# find_parents() find_parent() find_next_siblings() find_next_sibling()
# find_previous_siblings() find_previous_sibling() find_all_next()
# find_next() find_previous() find_all_previous()
print("########################################")
print(soup1.select('.container .header-left'))
print(soup1.select('ul li'))
print(soup1.select('#link'))
print(type(soup1.select('ul')[0]))
for ul in soup1.select('ul'):
    print(ul.select('li'))
    print(ul['id'])
    print(ul.attrs['id'])
for a in soup1.select('a'):
    print(a.get_text())