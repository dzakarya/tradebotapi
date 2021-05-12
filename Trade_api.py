import time
import requests
import json
import hmac
import hashlib
import urllib
ts = int(round(time.time() * 1000))

class trade():
    def __init__(self,api_key,secret_key):
        self.base_url = "https://indodax.com/tapi"
        self.secret_key = secret_key
        self.api_key = api_key

    def getInfo(self):
        payload = {
            "method" : "getInfo",
            "timestamp" : ts,
        }
        paybytes = urllib.parse.urlencode(payload).encode('utf8')
        sign = hmac.new(self.secret_key, paybytes, hashlib.sha512).hexdigest()
        head = {
            "Key" : self.api_key,
            "Sign" : sign,
        }

        r = requests.post(self.base_url, headers=head, data=payload)
        res = r.content.decode()
        res = json.loads(res)
        return res

    def getTicker(self,coin):
        base_url = "https://indodax.com"
        req = "/api/ticker/"
        end_point = base_url+req+coin
        r = requests.get(end_point)
        res = r.content.decode()
        res = json.loads(res)
        return res["ticker"]