import requests
import execjs

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=XXXX'
headers = {
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

js_file = open('wyyy.js',encoding='utf-8').read()
js_code = execjs.compile(js_file)
a={
    "ids": "[2110202909]",
    "level": "standard",
    "encodeType": "aac",
    "csrf_token": "XXXX"
}

resp = js_code.call('get_data',a)

data = {
    'params': resp['encText'],
    'encSecKey': resp['encSecKey'],
    }

print(resp)

res = requests.post(url=url, headers=headers, data=data)
music_url = res.json()['data'][0]['url']
print(music_url)

