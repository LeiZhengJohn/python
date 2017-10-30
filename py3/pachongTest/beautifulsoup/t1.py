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
		<div id="container">
			<div id="header-left">
				<img src="picture/logo.png" width="320" height="51"/>
			</div>
			<div id="header-right">
				<form action="" method="post">
				  <font color="#F8FFB2">用户名：</font><input type="text" name="username" /><br>
					<font color="#F8FFB2">密码：</font><input type="password" name="password" />
				  <input type="submit" value="登录">
				</form>
			</div>
			<div id="link">
				<h2>为您推荐</h2>
				<ul>
					<li><a href="main.html">本站主页</a></li>
					<li><a href="interduction.html">关于本站</a></li>
					<li><a href="database.html">数据库简介</a></li>
					<li><a href="function3.html">Blast</a></li>
					<li><a href="about.html">关于我们</a></li>
				</ul>
				<h2>友情链接</h2>
				<ul>
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
			<div id="ad">
				通知及广告
			</div>
			<p name="space" value="545">&nbsp;</p>
			<div id="footer">
				Copyright
			</div>
		</div>
'''
soup1 = BeautifulSoup(html1,'lxml')
#print(soup1.prettify())
print(soup1.title.string)
print(soup1.title)
print(type(soup1.title))
print(soup1.head)
print(soup1.p)
print(soup1.p.name)
print(soup1.p.attrs['name'])
print(soup1.p['value'])
print("*******************")
print(soup1.ul.li.a['href'])
print(soup1.ul.contents)
print(soup1.ul.children)
for i,child in enumerate(soup1.ul.children):
    print(i,child)
for j,child in enumerate(soup1.ul.descendants):
    print(j,child)
print("*******************")
print(soup1.a.parent)
for k,parent in enumerate(soup1.a.parents):
    print(k,parent)
print("####################################################")
for l,nbrother in enumerate(soup1.li.next_siblings):
    print(l,nbrother)
for m,pbrother in enumerate(soup1.li.previous_siblings):
    print(m,pbrother)
