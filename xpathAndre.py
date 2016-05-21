# -*- coding:utf-8 -*-
import zhilian
import re
from lxml import etree#导入xpath
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''在注释（SWSStringCutStart）中获取xpath，并添加一个自定义的div标签，采集div标签中的所有内容'''
# url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=python&p=1'
# zlspider = zhilian.spider()
# html = zlspider.getSource(url)
# # print html
# selector=etree.HTML(html, parser=None, base_url=None)
# links = selector.xpath('//*[@class="zwmc"]/div/a/@href')
# f = open('info2.txt','w')
# for link in links:
#     html1 = zlspider.getSource(link)
#     html2 = re.search('<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->', html1, re.S).group(1)
#     html3 = '<div class="require">' + html2 + '</div>'
#     # print html3
#     selector1 = etree.HTML(html3, parser=None, base_url=None)
#     datas = selector1.xpath('//div[@class="require"]')
#     for data in datas:
#         # print data
#         info = data.xpath('string(.)')
#         # context = info
#         # print info
#         context = info.replace('\n','').replace(' ','')
#         # context = info.replace(' ','')
#         # print context
#         # if context != '':
#         #     f.write('%s\n'%context)
#         f.write(context)
# f.close()
'''在注释（SWSStringCutStart）中获取xpath，采集p标签'''
url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=python&p=1'
zlspider = zhilian.spider()
html = zlspider.getSource(url)
# print html
selector=etree.HTML(html, parser=None, base_url=None)
links = selector.xpath('//*[@class="zwmc"]/div/a/@href')
# jobs = selector.xpath('//*[@class="zwmc"]/div/a/text()')
f = open('info3.txt','w')
print len(links)
for link in links:
    # f.write('%s\n' % link)
    html1 = zlspider.getSource(link)
    selector1 = etree.HTML(html1, parser=None, base_url=None)
    job = selector1.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')
    # print job[0]
    f.write('职位：%s\n'%job[0])
    f.write('%s\n' % link)
    html2 = re.search('<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->', html1, re.S).group(1)
    selector2 = etree.HTML(html2, parser=None, base_url=None)
    datas = selector2.xpath('//p')
    for data in datas:
        # print data
        info = data.xpath('string(.)')
        context = info
        # print info
        # context = info.replace('\n','').replace(' ','')
        # context = info.replace(' ','')
        # print context
        f.write('%s\n'%context)
        # f.write(context)
f.close()