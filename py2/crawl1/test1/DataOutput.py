import codecs
class DataOutput(object):
    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return()
        self.datas.append(data)
    def output_html(self):
        file=codecs.open('text.html','w',encoding='utf-8')
        file.write("<html>")
        file.write("<head><meta charset='utf-8'/></head>")
        file.write("<body>")
        file.write("<table>")
        for data in self.datas:
            file.write("<tr>")
            file.write("<td>%s</td>"%data['url'])
            file.write("<td>%s</td>"%data['title'])
            file.write("<td>%s</td>"%data['summary'])
            file.write("</tr>")
            self.datas.remove(data)
        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
        file.close()
