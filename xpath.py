# -*- coding:utf-8 -*-
import zhilian
from lxml import etree#导入xpath
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# html='''
# <!DOCTYPE html>
# <html>
# <head lang="en">
#     <meta charset="UTF-8">
#     <title>测试-常规用法</title>
# </head>
# <body>
# <div id="content">
#     <ul id="useful">
#         <li>这是第一条信息</li>
#         <li>这是第二条信息</li>
#         <li>这是第三条信息</li>
#     </ul>
#     <ul id="useless">
#         <li>不需要的信息1</li>
#         <li>不需要的信息2</li>
#         <li>不需要的信息3</li>
#     </ul>
#
#     <div id="url">
#         <a href="http://jikexueyuan.com">极客学院</a>
#         <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
#     </div>
# </div>
#
# </body>
# </html>
# '''
# selector=etree.HTML(html, parser=None, base_url=None)
#
# #提取文本
# context=selector.xpath('//*[@id="useful"]/li/text()')
# for each in context:
#     print each
# #结果显示：这是第一条信息
# #这是第二条信息
# #这是第三条信息
#
#
#
# #提取属性
# link=selector.xpath('//*[@id="url"]/a/@href')
# for each in link:
#     print each
# #结果显示：http://jikexueyuan.com
# #http://jikexueyuan.com/course/
#
#
#
# #提取标题
# title=selector.xpath('//*[@id="url"]/a/@title')
# print title[0]
# #结果显示：极客学院课程库

# url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=python&p=1'
# zlspider = zhilian.spider()
# html = zlspider.getSource(url)
# # print html
# selector=etree.HTML(html, parser=None, base_url=None)
# links = selector.xpath('//*[@class="zwmc"]/div/a/@href')
# f = open('info1.txt','w')
# for link in links:
#     html1 = zlspider.getSource(link)
#     # print html1
#     selector1 = etree.HTML(html1, parser=None, base_url=None)
#     # context = selector1.xpath('/html/body/div[6]/div[1]/div[1]/div/div/p/text()')
#     context = selector1.xpath('//*[@class="terminalpage-main clearfix"]/div/div[1]/p/text()')
#     for x in context:
#         # print x
#         # f.write('%s\n'%x)
#         # x = x.replace('\n','').replace(' ','')
#         f.writelines('%s\n'%x)
# f.close()


url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=python&p=1'
zlspider = zhilian.spider()
html = zlspider.getSource(url)
# print html
selector=etree.HTML(html, parser=None, base_url=None)
links = selector.xpath('//*[@class="zwmc"]/div/a/@href')
f = open('info.txt','w')
for link in links:
    html1 = zlspider.getSource(link)
    # print html1
    selector1 = etree.HTML(html1, parser=None, base_url=None)
    # / html / body / div[6] / div[1] / div[1] / div / div[1] / comment()[1]
    # / html / body / div[6] / div[1] / div[1] / div / div[1] / comment()[2]
    # datas = selector1.xpath('//*[@class="terminalpage-main clearfix"]/div/\
    # div[1][comment()[1]=" SWSStringCutEnd "]') #没输出
    datas = selector1.xpath('//*[@class="terminalpage-main clearfix"]/div/div[1]')
    for data in datas:
        # print data
        info = data.xpath('string(.)')
        context = info
        # print info
        # context = info.replace('\n','').replace(' ','')
        # context = info.replace(' ','')
        # print context
        # f.write('%s\n'%context)
        f.write(context)
f.close()