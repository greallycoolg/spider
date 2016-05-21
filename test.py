# -*- coding:utf-8 -*-
import requests
from lxml import etree  # 导入xpath
import os
import sys
import urllib

from requests.packages.urllib3 import Timeout

reload(sys)
sys.setdefaultencoding('utf-8')
'''不使用函数的方法获取极客学院python课程的视频'''
url = 'http://www.jikexueyuan.com/course/1373.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221542d29eed714b-062697066-424b0221-1fa400-1542d29eed814f%22%7D; stat_uuid=1462528923426943513999; sso_closebindpop=bindphone; BAIDU_SSP_lcr=https://www.baidu.com/link?url=H0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7&wd=&eqid=add9f6d80017992700000002573938db; looyu_id=455e31687747cc191e0895715fcb356cfe_20001269%3A5; uname=jike_zf8cqxng; uid=5018852; code=6XYTSE; authcode=9e43FQ%2Fjr1qQnDqQF0NWVpyx1BuIBdcEsx47Z0XfDIAGjTkCea8t%2FsIfS3L0vOOIYOARbKqo%2FwrlKYLiKwdgAywQusXpEbqor7tCN99Ht8SVjNE%2FHac4fY3yWlCGtJIfLg; level_id=1; is_expire=0; domain=4630978740; stat_fromWebUrl=; stat_ssid=1464147997513; _gat=1; _99_mon=%5B0%2C0%2C0%5D; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1462774293,1462774303,1462937442,1463367915; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1463543783; _ga=GA1.2.2107536999.1461046603; undefined=; stat_isNew=0; looyu_20001269=v%3A097eb922341b7f40d9c9fb1df4a1e3867f%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DH0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7%2526wd%253D%2526eqid%253Dadd9f6d80017992700000002573938db%2Cr%3A%2Cmon%3Ahttp%3A//m9106.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/'
}
response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
html = response.text
# print html
selector=etree.HTML(html, parser=None, base_url=None)
# links = selector.xpath('//*[@id="play_video_html5_api"]')
courseid = selector.xpath('//*[@class="orinagebtn"]/@course_id')[0]
# courseid = '2659'
# print courseid
jsonurl = 'http://www.jikexueyuan.com/course/downloadRes?course_id=' + courseid
downloadjson = requests.get(jsonurl, headers=headers).json()
print downloadjson
print type(downloadjson)
# type(downloadjson['data'])
if not downloadjson['data'] == {}:
    print downloadjson['data']['url']
else:
    print '此课时没有资料'
# zipdata = requests.get(downloadjson['data']['url']).content
# # print type(zipdata)
# with open('materials.zip', 'wb') as f:
#     f.write(zipdata)
# zipdata = requests.get(downloadjson['data']['url'], headers=headers, stream=True).raw
# # print type(zipdata)
# with open('materials.zip', 'wb') as f:
#     f.write(zipdata.read())
# urllib.urlretrieve(downloadjson['data']['url'],'materials.zip')


# if not os.path.isdir(coursename):
#     os.mkdir(coursename)
# print videoname
# print os.sep
# targetFile = coursename + os.sep + videoname + '.mp4'
# # video = requests.get(videolink).content
# # video = requests.get(videolink).text
# video = requests.get(videolink, stream=True).raw
# # with open('jike.mp4','wb') as f:
# with open(targetFile,'wb') as f:
#     f.write(video.read())

print 'haha'