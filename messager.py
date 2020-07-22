import urllib3
import json
from urllib.request import urlopen
url = '机器人webhook地址'
urllib3.disable_warnings()
http = urllib3.PoolManager()
text = {"content": "hello",
        "mentioned_list":["@all"]}
data = {'msgtype': 'text',
        'text':text}
#将字典数据编码为json数据
encoded_data = json.dumps(data).encode('utf-8')
#发送一个body的json数据
r = http.request('POST',url,body=encoded_data,
 headers={'Content-Type': 'application/json'})
