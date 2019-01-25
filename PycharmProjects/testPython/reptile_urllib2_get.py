# coding=utf-8
import urllib
import urllib2

values = {"uid": "3", "count": "20"}
data = urllib.urlencode(values)           #将字典格式的参数数据转换成格式编码后再传送给request对象
url = "http://api.test.sokafootball.com:8092/article/fetch"
geturl = url + "?" + data
request = urllib2.Request(geturl)
try:
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.HTTPError,e:
    print e.code
    print e.reason
except urllib2.URLError,e:
    print e.reason
else:
    print ("run is over")
