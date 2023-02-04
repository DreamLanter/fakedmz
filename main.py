# This is a sample Python script.
import hashlib
import json
import math
import random
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from typing import Union
from tqdm import tqdm, trange
import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
token_cache_path = f'/Users/wangchenxiang/code/python/fakedmz/token_cache.json'
def get_token(name):
    try:
        with open(token_cache_path) as f:
            d = json.load(f)
            value = d.get(name,"")
            print('get token',name,value)
            return value
    except:
        return ""
def update_token(name,value):
    try:
        with open(token_cache_path) as f:
            d = json.load(f)
    except:
        d = {}
    d[name] = value
    with open(token_cache_path,'w') as f:
        json.dump(d,f)
    print('update token', name, value)
#mi_token = '81c84030b02b79f353a376e2d5cb774b'
mi_token = get_token('mi_token')
def login_mi():
    response = requests.get(
        url="http://192.168.31.1/cgi-bin/luci/web/home",
        headers={
            "Host": "192.168.31.1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "http://192.168.31.1/cgi-bin/luci",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cookie": "__guid=86847064.4346738647225766000.1671804499294.1155; psp=admin|||2|||0; monitor_count=39",
        },
    )
    key = re.search("key: '(.+)'",response.text).group(1)
    deviceId = re.search("var deviceId = '(.+)'",response.text).group(1)
    def send_login_mi():
        try:
            nonce = f"0_{deviceId}_{math.floor(time.time())}_{math.floor(random.random()*10000)}"
            sha1 = lambda x: hashlib.sha1(x.encode()).hexdigest()
            password = sha1(nonce + sha1('038845tfm' + key))
            response = requests.post(
                url="http://192.168.31.1/cgi-bin/luci/api/xqsystem/login",
                headers={
                    "Host": "192.168.31.1",
                    "Connection": "keep-alive",
                    "Content-Length": "126",
                    "Accept": "*/*",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "http://192.168.31.1",
                    "Referer": "http://192.168.31.1/cgi-bin/luci/web/home",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "Cookie": "__guid=86847064.4346738647225766000.1671804499294.1155; psp=admin|||2|||0; monitor_count=40",
                },
                data={
                    "username": "admin",
                    "password": password,
                    "logtype": "2",
                    "nonce": nonce,
                },
            )
            token = response.json()['token']
            global mi_token
            mi_token = token
            update_token("mi_token",mi_token)
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
    send_login_mi()
def get_mi_upnp():
    try:
        response = requests.get(
            url=f"http://192.168.31.1/cgi-bin/luci/;stok={mi_token}/api/xqsystem/upnp",
            headers={
                "Host": "192.168.31.1",
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": f"http://192.168.31.1/cgi-bin/luci/;stok={mi_token}/web/prosetting/upnp",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cookie": "__guid=86847064.4346738647225766000.1671804499294.1155; psp=admin|||2|||0; monitor_count=43",
            },
        )
        return list(map(lambda x:int(x['rport']),response.json()['list']))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


cookies = {
    "Cookie": "sid=64c343d7bfc223809f756df8489ea8d39e91bc5dffcaee394e996968e842c394:Login:id=1",
    "sysauth": get_token('sysauth')
}
token = get_token('token')
def login():
    def login_1():
        try:
            response = requests.post(
                url="http://192.168.1.1/cgi-bin/luci",
                headers={
                    "Host": "192.168.1.1",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Origin": "http://192.168.1.1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Referer": "http://192.168.1.1/cgi-bin/luci",
                    "Content-Length": "28",
                },
                cookies=cookies,
                data={
                    "username": "useradmin",
                    "psd": "ahiz7",
                },
                allow_redirects=False
            )
            ckstr = response.headers.get("Set-Cookie")
            ckstr = ckstr[ckstr.find('=')+1:ckstr.find(';')]
            cookies['sysauth'] = ckstr
            update_token('sysauth',ckstr)
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def login_2():
        try:
            response = requests.get(
                url="http://192.168.1.1/cgi-bin/luci/admin/home",
                headers={
                    "Host": "192.168.1.1",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
                    "Referer": "http://192.168.1.1/cgi-bin/luci/",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                },
                cookies=cookies
            )
            text = response.text
            tk = re.search("token: '(.+)'",text).group(1)
            global token
            token = tk
            update_token('token',token)
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
    login_1()
    login_2()
def getall():
    req = requests.get("http://192.168.1.1/cgi-bin/luci/admin/settings/pmDisplay",
                       headers={
                           "Accept": "*/*",
                           "Accept-Encoding": "gzip, deflate",
                           "Accept-Language": "en-US,en;q=0.9",
                           "Connection": "keep-alive",
                           "Host": "192.168.1.1",
                           "Referer": "http://192.168.1.1/cgi-bin/luci/admin/settings/portmap_list",
                           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"
                       },
                       cookies=cookies,
                       auth=(),
                       )
    return req.json()


def setSingle(srv_name, op):
    if op not in ("del", "disable", "enable"):
        return
    req = requests.post("http://192.168.1.1/cgi-bin/luci/admin/settings/pmSetSingle",
                        data=f'token={token}&op={op}&srvname={srv_name}',
                        headers={
                            "Accept": "*/*",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Connection": "keep-alive",
                            "Content-Length": "80",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "Host": "192.168.1.1",
                            "Origin": "http://192.168.1.1",
                            "Referer": "http://192.168.1.1/cgi-bin/luci/admin/settings/portmap_list",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"
                        },
                        cookies=cookies,
                        auth=(),
                        )
    if req.json()['retVal'] < 0:
        raise Exception(req.json()['retVal'])

def add(ip:str,port:int):
    req = requests.post("http://192.168.1.1/cgi-bin/luci/admin/settings/pmSetSingle",
                  data=f'token={token}&op=add&srvname={port}&client={ip}&protocol=BOTH&exPort={port}&inPort={port}',
                  headers={
                      "Accept": "*/*",
                      "Accept-Encoding": "gzip, deflate",
                      "Accept-Language": "en-US,en;q=0.9",
                      "Connection": "keep-alive",
                      "Content-Length": "128",
                      "Content-Type": "application/x-www-form-urlencoded",
                      "Host": "192.168.1.1",
                      "Origin": "http://192.168.1.1",
                      "Referer": "http://192.168.1.1/cgi-bin/luci/admin/settings/portmap_config",
                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"
                  },
                  cookies=cookies,
                  auth=(),
                  )
    if req.json()['retVal'] < 0:
        raise Exception(req.json()['retVal'])
try:
    upnp = get_mi_upnp()
except:
    login_mi()
    upnp = get_mi_upnp()
important_port = [
    6881,
]
for port in important_port:
    if port not in upnp:
        upnp.insert(0, port)

upnp_set = set(upnp)

exists_port = set()
try:
    a = getall()
except:
    login()
    a = getall()
print('remove all exists map')
for x in range(1, a['count'] + 1):
    port = a[f'pmRule{x}']['inPort']
    exists_port.add(port)

un_exists_port = exists_port - upnp_set

with tqdm(total=len(un_exists_port)) as pbar:
    for port in un_exists_port:
        pbar.set_description(f'remove {port}')
        setSingle(port, 'del')
        pbar.update()

if False:
    with tqdm(total=a['count']) as pbar:
        for x in range(1,a['count']+1):
            name = a[f'pmRule{x}']['desp']
            setSingle(name,'del')
            pbar.set_description(f"remove {name}")
            pbar.update()

need_add = [ x for x in upnp if x not in exists_port]

with tqdm(total=len(need_add)) as pbar:
    for port in need_add:
        add("192.168.1.56",port)
        pbar.set_description(f'set {port}')
        pbar.update(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
