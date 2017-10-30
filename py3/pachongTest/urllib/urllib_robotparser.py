from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
print(rrate.requests+'|'+rrate.seconds)
print(rp.crawl_delay("*"))
print(rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
print(rp.can_fetch("*", "http://www.musi-cal.com/"))
