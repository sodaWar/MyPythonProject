# coding=utf-8
import urllib.request
import urllib.parse

values = {"uid": "3", "count": "20"}
data = urllib.parse.urlencode(values)           #将字典格式的参数数据转换成格式编码后再传送给request对象
url = "http://api.test.sokafootball.com:8092/article/fetch"
geturl = url + "?" + data
try:
    response = urllib.request.urlopen(geturl)
    print (response.read())
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
else:
    print ("run is over")
