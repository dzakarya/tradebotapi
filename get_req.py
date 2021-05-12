import requests
import json
base_url = "https://indodax.com"
req = "/api/ticker/dogeidr"
end_point = base_url+req
r = requests.get(end_point)
res = r.content.decode()
res = json.loads(res)
print (res["ticker"]["high"])