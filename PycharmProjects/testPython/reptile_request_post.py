import requests
import json
import hashlib

password = "naiwu3425"
password_md5 = hashlib.md5(password)
password_encrypt = password_md5.hexdigest()

values = {
        "chlId": 0,
        "deviceId": "5f6068091532d12db68c951141ffdb83",
        "identity": "11111@qq.com",
        "os": 1,
        "password": "e10adc3949ba59abbe56e057f20f883e",
        "sex": 0,
        "type": 1,
        "value_type": 1
}
delivery_data = json.dumps(values)
delivery_url = "http://api.test.sokafootball.com//login/v2/email"
delivery_headers = {"Content-Type": "application/json"}
r = requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)
print r.status_code
print r.text
print r.encoding
