import cookielib
import urllib2

res_filename = "D:\Pycharm\cookie.txt"
cookie = cookielib.MozillaCookieJar(filename = res_filename)    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
handler = urllib2.HTTPCookieProcessor(cookie)     #创建Cookie处理器
opener = urllib2.build_opener(handler)        #通过handler来构建opener
response = opener.open("http://www.baidu.com")      #创建一个请求
cookie.save(ignore_discard=True,ignore_expires=True)       #保存cookie到文件，第一个参数是cookie被丢弃了也要保存下来，第二个是
#如果cookie已存在，则覆盖原文件写入
