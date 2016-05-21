# -*- coding:utf-8 -*-
import requests
from lxml import etree  # 导入xpath
import os
import sys
import time
import json
from multiprocessing import Pool as ThreadPool
# from requests.packages.urllib3 import Timeout

reload(sys)
sys.setdefaultencoding('utf-8')
'''不使用函数的方法获取极客学院python课程的视频'''
# url = 'http://www.jikexueyuan.com/course/1373.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
#     'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221542d29eed714b-062697066-424b0221-1fa400-1542d29eed814f%22%7D; stat_uuid=1462528923426943513999; sso_closebindpop=bindphone; BAIDU_SSP_lcr=https://www.baidu.com/link?url=H0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7&wd=&eqid=add9f6d80017992700000002573938db; looyu_id=455e31687747cc191e0895715fcb356cfe_20001269%3A5; uname=jike_zf8cqxng; uid=5018852; code=6XYTSE; authcode=9e43FQ%2Fjr1qQnDqQF0NWVpyx1BuIBdcEsx47Z0XfDIAGjTkCea8t%2FsIfS3L0vOOIYOARbKqo%2FwrlKYLiKwdgAywQusXpEbqor7tCN99Ht8SVjNE%2FHac4fY3yWlCGtJIfLg; level_id=1; is_expire=0; domain=4630978740; stat_fromWebUrl=; stat_ssid=1464147997513; _gat=1; _99_mon=%5B0%2C0%2C0%5D; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1462774293,1462774303,1462937442,1463367915; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1463543783; _ga=GA1.2.2107536999.1461046603; undefined=; stat_isNew=0; looyu_20001269=v%3A097eb922341b7f40d9c9fb1df4a1e3867f%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DH0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7%2526wd%253D%2526eqid%253Dadd9f6d80017992700000002573938db%2Cr%3A%2Cmon%3Ahttp%3A//m9106.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/'
# }
# response = requests.get(url,headers=headers)
# # response.encoding = 'utf-8'
# html = response.text
# # print html
# selector=etree.HTML(html, parser=None, base_url=None)
# # links = selector.xpath('//*[@id="play_video_html5_api"]')
# videolink = selector.xpath('//*[@id="play_video"]/source/@src')[0]
# coursename = selector.xpath('//*[@id="palyer-box"]/h1/text()')[0]
# videoname = selector.xpath('//*[@class="playing"]/h2/a/text()')[0]
# if not os.path.isdir(coursename):
#     os.mkdir(coursename)
# print videoname
# # print os.sep
# targetFile = coursename + os.sep + videoname + '.mp4'
# # # video = requests.get(videolink).content
# # # video = requests.get(videolink).text
# # video = requests.get(videolink, stream=True).raw
# # # with open('jike.mp4','wb') as f:
# # with open(targetFile,'wb') as f:
# #     f.write(video.read())

'''使用函数的方法获取极客学院相关课程的视频'''


def getHTML(url, type='text'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221542d29eed714b-062697066-424b0221-1fa400-1542d29eed814f%22%7D; stat_uuid=1462528923426943513999; sso_closebindpop=bindphone; BAIDU_SSP_lcr=https://www.baidu.com/link?url=H0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7&wd=&eqid=add9f6d80017992700000002573938db; looyu_id=455e31687747cc191e0895715fcb356cfe_20001269%3A5; uname=jike_zf8cqxng; uid=5018852; code=6XYTSE; authcode=9e43FQ%2Fjr1qQnDqQF0NWVpyx1BuIBdcEsx47Z0XfDIAGjTkCea8t%2FsIfS3L0vOOIYOARbKqo%2FwrlKYLiKwdgAywQusXpEbqor7tCN99Ht8SVjNE%2FHac4fY3yWlCGtJIfLg; level_id=1; is_expire=0; domain=4630978740; stat_fromWebUrl=; stat_ssid=1464147997513; _gat=1; _99_mon=%5B0%2C0%2C0%5D; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1462774293,1462774303,1462937442,1463367915; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1463543783; _ga=GA1.2.2107536999.1461046603; undefined=; stat_isNew=0; looyu_20001269=v%3A097eb922341b7f40d9c9fb1df4a1e3867f%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DH0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7%2526wd%253D%2526eqid%253Dadd9f6d80017992700000002573938db%2Cr%3A%2Cmon%3Ahttp%3A//m9106.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/'
    }
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    #     'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221542d29eed714b-062697066-424b0221-1fa400-1542d29eed814f%22%7D; stat_uuid=1462528923426943513999; sso_closebindpop=bindphone; BAIDU_SSP_lcr=https://www.baidu.com/link?url=H0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7&wd=&eqid=add9f6d80017992700000002573938db; looyu_id=455e31687747cc191e0895715fcb356cfe_20001269%3A5; uname=jike_zf8cqxng; uid=5018852; code=6XYTSE; authcode=9e43FQ%2Fjr1qQnDqQF0NWVpyx1BuIBdcEsx47Z0XfDIAGjTkCea8t%2FsIfS3L0vOOIYOARbKqo%2FwrlKYLiKwdgAywQusXpEbqor7tCN99Ht8SVjNE%2FHac4fY3yWlCGtJIfLg; level_id=1; is_expire=0; domain=4630978740; stat_fromWebUrl=; stat_ssid=1464147997513; _gat=1; _99_mon=%5B0%2C0%2C0%5D; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1462774293,1462774303,1462937442,1463367915; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1463543783; _ga=GA1.2.2107536999.1461046603; undefined=; stat_isNew=0; looyu_20001269=v%3A097eb922341b7f40d9c9fb1df4a1e3867f%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DH0HLymErTltdS4i1wdH4vHdot4tljDGb-Hqw5AatOptGoEYeXyzvfIjEgiuR7oh7%2526wd%253D%2526eqid%253Dadd9f6d80017992700000002573938db%2Cr%3A%2Cmon%3Ahttp%3A//m9106.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/',
    #     'Referer': url
    # }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if type == 'text':
        return response.text
    elif type == 'json()':
        return response.json()


# def getVideo(url, coursename, videoname, line='ss=1'):
#     print '    视频：' + videoname + ',' + videourl
#     print '    Downloading...'
#     url.replace('ss=1', line)
#     video = requests.get(url, stream=True, timeout=10).raw
#     # print 'get raw format data'
#     if not os.path.isdir(coursename):
#         os.mkdir(coursename)
#     targetfile = coursename + os.sep + videoname + '.mp4'
#     with open(targetfile, 'wb') as f:
#         f.write(video.read())
#     print '    Successfull!!'


def getVideo(kwargs):
    lessonurl = kwargs['lessonurl']
    lessonurl2 = kwargs['lessonurl2']
    coursename = kwargs['coursename']
    lessonhtml = getHTML(lessonurl)
    lessonhtml2 = getHTML(lessonurl2)
    videourl = getxpathValue(lessonhtml, '//*[@id="play_video"]/source/@src')[0]
    videourl2 = getxpathValue(lessonhtml2, '//*[@id="play_video"]/source/@src')[0]
    videoname = getxpathValue(lessonhtml, '//*[@class="playing"]/h2/a/text()')[0]
    videoname = videoname.replace('/', ' ').replace('"', ' ').replace('?', ' ')
    # print '    视频：' + videoname + ',' + videourl
    print '    Downloading...'
    # videourl.replace('ss=1', line)
    dirname = r'F:\极客学院\%s'%coursename
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    targetfile = r'F:\极客学院\%s\%s.mp4'%(coursename,videoname)
    with open(targetfile, 'wb') as f:
        try:
            video = requests.get(videourl, stream=True, timeout=10).raw
            # print 'get raw format data'
            f.write(video.read())
            print '    Successfull!!' + '    视频：' + videoname + ',' + videourl
        except (requests.packages.urllib3.exceptions.ReadTimeoutError, requests.exceptions.RequestException), e:
            print e
            print '切换线路2...'
            try:
                video = requests.get(videourl2, stream=True, timeout=10).raw
                # print 'get raw format data'
                f.write(video.read())
                print '    Successfull!!' + '    视频：' + videoname + ',' + videourl
            except (requests.packages.urllib3.exceptions.ReadTimeoutError, requests.exceptions.RequestException), e:
                print '请手动下载^_^,%s,%s'%(coursename, videoname)


def getxpathValue(html, xxpath):
    selector = etree.HTML(html, parser=None, base_url=None)
    values = selector.xpath(xxpath)
    return values


def getArchive(downloadjson, coursename):
    if not downloadjson['data'] == {}:
        print '    downloading....' + '资料：' + downloadjson['data']['url']
        zipdata = requests.get(downloadjson['data']['url']).content
        # print type(zipdata)
        # dirname = coursename + os.sep + '资料'
        dirname = r'F:\极客学院\%s\资料'%coursename
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        # targetfile = dirname + os.sep + coursename + ' code.zip'
        targetfile = r'%s\%s code.zip'%(dirname,coursename)
        with open(targetfile, 'wb') as f:
            f.write(zipdata)
        print 'successfull!  ' + coursename
    else:
        print '此课时没有资料  ' + coursename


def getVideoJson(parturl,start,end):
    args = []
    for x in range(start, int(end+1)):
        pyurl = parturl + str(x)
        html = getHTML(pyurl)
        courseurls = getxpathValue(html, '//*[@class="lesson-info-h2"]/a/@href')
        print len(courseurls)
        for courseurl in courseurls:
            # courseurl = 'http://www.jikexueyuan.com/course/2635.html'
            coursehtml = getHTML(courseurl)
            # courseid = getxpathValue(lessonhtml, '//*[@class="orinagebtn"]/@course_id')[0]
            coursename = getxpathValue(coursehtml, '//*[@id="palyer-box"]/h1/text()')[0]
            coursename = coursename.replace('/', ' ').replace('"', ' ')
            print coursename + '：' + courseurl
            lessonurls = getxpathValue(coursehtml, '//*[@class="text-box"]/h2/a/@href')
            for lessonurl in lessonurls:
                lessonurl2 = lessonurl.replace('ss=1', 'ss=2')
                args.append({'lessonurl':lessonurl,'lessonurl2':lessonurl2,'coursename':coursename})
    return args


def getArchiveJson(parturl,start,end):
    pool = ThreadPool(30)
    for x in range(start, int(end+1)):
        # args2 = []
        pyurl = parturl + str(x)
        html = getHTML(pyurl)
        courseurls = getxpathValue(html, '//*[@class="lesson-info-h2"]/a/@href')
        print len(courseurls)
        for courseurl in courseurls:
            # courseurl = 'http://www.jikexueyuan.com/course/2635.html'
            coursehtml = getHTML(courseurl)
            # courseid = getxpathValue(lessonhtml, '//*[@class="orinagebtn"]/@course_id')[0]
            coursename = getxpathValue(coursehtml, '//*[@id="palyer-box"]/h1/text()')[0]
            coursename = coursename.replace('/', ' ').replace('"', ' ')
            print coursename + '：' + courseurl
            courseid = getxpathValue(coursehtml, '//*[@class="videobox player-video"]/@course_id')[0]
            jsonurl = 'http://www.jikexueyuan.com/course/downloadRes?course_id=' + courseid
            downloadjson = getHTML(jsonurl, type='json()')
            pool.apply_async(getArchive,args=(downloadjson, coursename))
    pool.close()
    pool.join()


'''单线程'''
# if __name__ == '__main__':
#     time1 = time.time()
#     for x in range(1, 7):
#         # pyurl = 'http://www.jikexueyuan.com/course/python/?pageNum=' + str(x)
#         pyurl = 'http://www.jikexueyuan.com/course/webbase/?pageNum=' + str(x)
#         html = getHTML(pyurl)
#         courseurls = getxpathValue(html, '//*[@class="lesson-info-h2"]/a/@href')
#         print len(courseurls)
#         for courseurl in courseurls:
#             # courseurl = 'http://www.jikexueyuan.com/course/1373.html' #python 数据库连接
#             # courseurl = 'http://www.jikexueyuan.com/course/923.html' #python web开发
#             # courseurl = 'http://www.jikexueyuan.com/course/943.html'
#             coursehtml = getHTML(courseurl)
#             # courseid = getxpathValue(lessonhtml, '//*[@class="orinagebtn"]/@course_id')[0]
#             courseid = getxpathValue(coursehtml, '//*[@class="videobox player-video"]/@course_id')[0]
#             jsonurl = 'http://www.jikexueyuan.com/course/downloadRes?course_id=' + courseid
#             downloadjson = getHTML(jsonurl, type='json()')
#             coursename = getxpathValue(coursehtml, '//*[@id="palyer-box"]/h1/text()')[0]
#             print coursename + '：' + courseurl
#             lessonurls = getxpathValue(coursehtml, '//*[@class="text-box"]/h2/a/@href')
#             for lessonurl in lessonurls:
#                 lessonhtml = getHTML(lessonurl)
#                 videourl = getxpathValue(lessonhtml, '//*[@id="play_video"]/source/@src')[0]
#                 videoname = getxpathValue(lessonhtml, '//*[@class="playing"]/h2/a/text()')[0]
#                 videoname = videoname.replace('/',' ').replace('"',' ')
#                 try:
#                     getVideo(videourl, coursename, videoname)
#                 except Exception, e:
#                     print e
#                     print '切换线路2...'
#                     try:
#                         getVideo(videourl, coursename, videoname, line='ss=2')
#                     except Exception, e:
#                         print  e
#                         print '*^﹏^* give up 手动获取吧！！'
#                     continue
#             getArchive(downloadjson, coursename)
#             # exit()
#     time2 = time.time()
#     print '花费：' + str(time2 - time1)
#     # videoname = getxpathValue(html, '//*[@class="playing"]/h2/a/text()')[0]
#     # getVideo(videolink, coursename, videoname)

'''多线程'''
if __name__ == '__main__':
    time1 = time.time()
    # args = []
    # # args2 = []
    # for x in range(1, 7):
    #     # pyurl = 'http://www.jikexueyuan.com/course/python/?pageNum=' + str(x)
    #     pyurl = 'http://www.jikexueyuan.com/course/clouddata/?pageNum=' + str(x)
    #     html = getHTML(pyurl)
    #     courseurls = getxpathValue(html, '//*[@class="lesson-info-h2"]/a/@href')
    #     print len(courseurls)
    #     for courseurl in courseurls:
    #         # courseurl = 'http://www.jikexueyuan.com/course/1373.html' #python 数据库连接
    #         # courseurl = 'http://www.jikexueyuan.com/course/923.html' #python web开发
    #         # courseurl = 'http://www.jikexueyuan.com/course/943.html'
    #         # courseurl = 'http://www.jikexueyuan.com/course/2635.html'
    #         coursehtml = getHTML(courseurl)
    #         # courseid = getxpathValue(lessonhtml, '//*[@class="orinagebtn"]/@course_id')[0]
    #         courseid = getxpathValue(coursehtml, '//*[@class="videobox player-video"]/@course_id')[0]
    #         jsonurl = 'http://www.jikexueyuan.com/course/downloadRes?course_id=' + courseid
    #         downloadjson = getHTML(jsonurl, type='json()')
    #         coursename = getxpathValue(coursehtml, '//*[@id="palyer-box"]/h1/text()')[0]
    #         coursename = coursename.replace('/', ' ').replace('"', ' ')
    #         print coursename + '：' + courseurl
    #         lessonurls = getxpathValue(coursehtml, '//*[@class="text-box"]/h2/a/@href')
    #         for lessonurl in lessonurls:
    #             # lessonurl2 = lessonurl.replace('ss=1', 'ss=2')
    #             lessonhtml = getHTML(lessonurl)
    #             # lessonhtml2 = getHTML(lessonurl2)
    #             videourl = getxpathValue(lessonhtml, '//*[@id="play_video"]/source/@src')[0]
    #             # videourl2 = getxpathValue(lessonhtml2, '//*[@id="play_video"]/source/@src')[0]
    #             videoname = getxpathValue(lessonhtml, '//*[@class="playing"]/h2/a/text()')[0]
    #             videoname = videoname.replace('/', ' ').replace('"', ' ').replace('?', ' ')
    #             args.append({'videourl':videourl,'coursename':coursename,'videoname': videoname})
    #             # args2.append({'videourl':videourl2,'coursename':coursename,'videoname': videoname})
    #             getArchive(downloadjson, coursename)

    # args = getVideoJson('http://www.jikexueyuan.com/course/mysql//?pageNum=', 1, 1)
    # f = open('video.json','wb')
    # json.dump(args, f)
    # f.close()
    # print args[0]

    # getArchiveJson('http://www.jikexueyuan.com/course/mysql//?pageNum=', 1, 1)

    with open('video.json', 'rb') as f:
        args = json.load(f)
    # print type(args)
    print len(args)
    # pool = ThreadPool(4)
    pool = ThreadPool(30)
    # pool.map(getVideo, args)
    pool.map_async(getVideo, args)
    pool.close()
    pool.join()

    time2 = time.time()
    print '花费：' + str(time2 - time1)

'''单个url获取'''
# if __name__ == '__main__':
#     courseurl = 'http://www.jikexueyuan.com/course/2635.html'
#     coursehtml = getHTML(courseurl)
#     # courseid = getxpathValue(lessonhtml, '//*[@class="orinagebtn"]/@course_id')[0]
#     courseid = getxpathValue(coursehtml, '//*[@class="videobox player-video"]/@course_id')[0]
#     jsonurl = 'http://www.jikexueyuan.com/course/downloadRes?course_id=' + courseid
#     downloadjson = getHTML(jsonurl, type='json()')
#     coursename = getxpathValue(coursehtml, '//*[@id="palyer-box"]/h1/text()')[0]
#     print coursename + '：' + courseurl
#     lessonurls = getxpathValue(coursehtml, '//*[@class="text-box"]/h2/a/@href')
#     for lessonurl in lessonurls:
#         lessonhtml = getHTML(lessonurl)
#         videourl = getxpathValue(lessonhtml, '//*[@id="play_video"]/source/@src')[0]
#         videoname = getxpathValue(lessonhtml, '//*[@class="playing"]/h2/a/text()')[0]
#         videoname = videoname.replace('/',' ').replace('"',' ')
#         try:
#             getVideo(videourl, coursename, videoname)
#         except Exception, e:
#             print e
#             print '切换线路2...'
#             try:
#                 getVideo(videourl, coursename, videoname, line='ss=2')
#             except Exception, e:
#                 print  e
#                 print '*^﹏^* give up 手动获取吧！！'
#             continue
#     getArchive(downloadjson, coursename)
