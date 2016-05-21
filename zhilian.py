#-*-coding:utf8-*-
import requests
import urllib2
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# sys.setdefaultencoding('ISO-8859-1')

# response = requests.get('http://www.zhaopin.com/')
# # print response.encoding
# # print response.text.encode('ISO-8859-1').decode('utf-8')
# response.encoding = 'utf-8'
# print response.text

# request = urllib2.Request('http://www.zhaopin.com/')
# request.add_header('User-Agent', 'fake-client')
# response = urllib2.urlopen(request)
# print response.read()

class spider(object):
    def __init__(self):
        print '开始爬取网页....'
    def getSource(self,url):
        html = requests.get(url)
        html.encoding = 'utf-8'
        # print type(html.text)
        return html.text
        # return html.text.encode('ISO-8859-1').decode('utf-8')
if __name__ == '__main__':
    # url = 'http://www.zhaopin.com/'
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=python&p=1'
    zlspider = spider()
    html = zlspider.getSource(url)
    everyjob = re.findall('(<td class="zwmc".*?</td>)',html,re.S)
    for x in everyjob:
        link = re.search('href="(.*?)"',x,re.S).group(1)
        print link
        html2 = zlspider.getSource(link)
        eachdetail = re.search('<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->',html2,re.S).group(1)
        details = re.findall('<p>(.*?)</p>',eachdetail,re.S)
        for i in details:
            print re.sub('<.*?br.*?>|&nbsp|<.*?span.*?>','',i)
            # print i.replace('&nbsp','').replace('<br/>','').replace('<br>','')
            # print i