import DataOutput
import HtmlDownloader
import UrlManager
import HtmlParser
class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = DataOutput.DataOutput()
    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print "already%slinks"%self.manager.old_url_size()
            except Exception as e:
                print e
        self.output.output_html()
if __name__=="__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
