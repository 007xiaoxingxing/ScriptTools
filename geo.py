# -*- coding: utf-8 -*-

import requests
import json
url = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=baidu_map_ak'

address = "成都市"

req_url = url % address

res = requests.get(req_url).text
res_obj = json.loads(res)
lng = res_obj['result']['location']['lng']
lat = res_obj['result']['location']['lat']
print(lng, lat)

