# coding by Tamsis X Code
# https://github.com/Kaii-Devv
# repositori ds2play

from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED
import requests
import string
import random
import re
import time
class ds:
    def __init__(self,proxy = False):
        self.u_proxy = proxy
        self.d_headers = {'Range': 'bytes=0-', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', 'Referer': 'https://dooood.com/','Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}
    def get(self,url):
        link = 'https://d0o0d.com/e/'+url.split('/')[-1]
        if not self.u_proxy:
            try:
                pass_md5 = re.search("/pass_md5/(.*?)', function",requests.get(link,headers={'referer': link, 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.9.0'}).text).group(1)
                url_pass_md5 = 'https://d0o0d.com/pass_md5/'+pass_md5
                video_delivery = requests.get(url_pass_md5,headers={"referer": link,"accept-encoding": "gzip","cookie": "lang=1; referer=","user-agent": "okhttp/4.9.0"}).text
                self.url = video_delivery+"".join([random.choice(string.ascii_letters) for _ in range(10)])+"?token="+url_pass_md5.split("/")[-1]+"&expiry="+str(round(time.time() + 24 * 60 *60,2)).replace('.','')
                self.proxy = False
                return self
            except Exception as e: raise TypeError('[ error ] Url doodstream not valid')
        if self.u_proxy:
            try:
                tok=url.split('/')[-1]
                proxylist = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text.split("\r\n")
                hasil={}
                with ThreadPoolExecutor(max_workers=20) as pool:
                    for proxy in proxylist:
                        pool.submit(self.check, proxy, tok,hasil,pool)
                self.url = hasil['url']
                self.response = hasil['content']
                return self
            except Exception as e:raise TypeError('[error] Url doodstream not valid')
    def content(self):
        if self.u_proxy:raise TypeError('[error] proxy True not suport .content()!! try .response')
        url = self.url
        result = requests.get(url,proxies=self.proxy,headers=self.d_headers,stream=True)
        return result
    def check(self,proxy,tok,hasil,pool):
        if len(str(hasil))>5:return
        proxy = {
    'http': 'socks5://'+proxy,
    'https': 'socks5://'+proxy
}
        try:
            ses=requests.Session()
            host= 'https://d0o0d.com'
            ses.proxies.update(proxy)
            log2=ses.get(host+"/e/"+tok,headers={'Host': 'd0o0d.com', 'referer': 'https://d0o0d.com/e/', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.9.0'},timeout=3)
            if not 'ddos' in log2.text.lower():
                link=host+"/pass_md5/"+re.search("/pass_md5/(.*?)', function",str(log2.text)).group(1)
                url = ses.get(link,headers={"Host": host.replace('https://',''),"referer": log2.url,"accept-encoding": "gzip","cookie": "lang=1","user-agent": "okhttp/4.9.0"},timeout=3).text+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+"?token="+link.split("/")[-1]+"&expiry=1"+"".join([str(random.randrange(1,9)) for _ in range(12)])
                content = ses.get(url,headers={'Range': 'bytes=0-', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', 'Referer': 'https://dooood.com/', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'},stream=True,timeout=3)
                hasil.update({'url':url,'content':content})
                pool.shutdown()
            else:pass
        except Exception as e :pass
# Exc
# print(ds(proxy=True).get('https://doodstream.com/d/ntp9hx999vsz').response)
# print(ds().get('https://doodstream.com/d/ntp9hx999vsz').content())
