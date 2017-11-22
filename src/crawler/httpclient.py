#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# resp = requests.get("http://www.jjxsw.com/txt/Young/index_275.html")
# print(resp.status_code, resp.content)
# tmp = BeautifulSoup(resp.content)
# tmp.find_all()

host_url = "http://www.jjxsw.com"
path = "/txt/Young/index_275.html"
encode_type = "gb18030"
response = requests.get(host_url+path)
response.encoding = encode_type
soup = BeautifulSoup(response.text, "html.parser")

# print('小说'.encode(encode_type) in soup.title.prettify(encode_type))
# print(soup.title.encode(encode_type))
item_list = soup.find_all(attrs={"class": "listbg"})
for each in item_list:
    print(host_url + each.find("a").get('href'))

def getMainSoftIntro(url):
    response = requests.get(url)
    response.encoding = encode_type
    soup = BeautifulSoup(response.text, "html.parser")
    tmp = soup.find(id="mainSoftIntro")
    print(tmp.text)