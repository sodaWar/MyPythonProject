import requests

values = {"uid": "3", "count": "20"}
re_url = "http://api.test.sokafootball.com:8092/article/fetch"
r = requests.get(url = re_url,params = values)
end = r.text

print (r.url)
print (end)
