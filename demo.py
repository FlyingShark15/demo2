#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Will  2018/8/1


import requests
import json
url = "https://movie.douban.com/explore#!type=movie&tag=%E7%BB%8F%E5%85%B8&sort=time&page_limit=20&page_start=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
}
response = requests.get(url, headers=headers)
r = response.content.decode()
print(type(r))



