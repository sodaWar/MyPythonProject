# coding=utf-8
import urllib.request
from http import cookiejar

cookie = cookiejar.CookieJar()    #声明一个CookieJar对象实例来保存cookie
handler = urllib.request.HTTPCookieProcessor(cookie) #利用HTTPCookieProcessor对象来创建cookie处理器
opener = urllib.request.build_opener(handler)   #通过handler来构建opener
response = opener.open("http://www.baidu.com")
for item in cookie:
    print ("Name = " + item.name)
    print ("Value = "+item.value)





