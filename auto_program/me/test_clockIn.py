from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import schedule
import requests
import logging
import time
import json
listCookies = [{"domain": ".yunzhijia.com", "httpOnly": 'true', "name": "cn", "path": "/", "secure": 'false', "value": "61ee5b7ce4b051b535e2473a"}, {"domain": "www.yunzhijia.com", "httpOnly": 'false', "name": "sync_networkid", "path": "/", "secure": 'true', "value": "61ee5b7ce4b051b535e2473a"}, {"domain": ".yunzhijia.com", "httpOnly": 'false', "name": "__loginType", "path": "/", "secure": 'false', "value": ""}, {"domain": "www.yunzhijia.com", "httpOnly": 'false', "name": "webLappToken", "path": "/", "secure": 'false', "value": "\"RTXcirUwxXdnd0q%2FsT%2FxQ%2FFZjwhZJtOMKBA09Y9hUzCcZU76UZ8SWYZ6PMLY82TgQMuRr94q5Y7U5xjLnPxt%2BQ%2ByFoOrLb3VvMOwlAT12Xs%3D\""}, {"domain": ".yunzhijia.com", "httpOnly": 'false', "name": "Hm_lpvt_a96914087b350d1aa86c96cdbf56d5e5", "path": "/", "secure": 'false', "value": "1667210405"}, {"domain": "www.yunzhijia.com", "httpOnly": 'true', "name": "cn", "path": "/", "sameSite": "None", "secure": 'true', "value": "61ee5b7ce4b051b535e2473a"}, {"domain": ".yunzhijia.com", "httpOnly": 'true', "name": "cd", "path": "/", "secure": 'false', "value": "yunzhijia.com"}, {"domain": ".yunzhijia.com", "expiry": 1667218409, "httpOnly": 'true', "name": "gl", "path": "/", "secure": 'false', "value": "84b38294-11d4-4721-8341-8af43ba30099"}, {"domain": ".yunzhijia.com", "httpOnly": 'true', "name": "at", "path": "/", "sameSite": "None", "secure": 'true', "value": "787d9f01-12f4-477e-a0b2-17f197c22cda"}, {"domain": "www.yunzhijia.com", "httpOnly": 'false', "name": "sync_userid", "path": "/", "secure": 'true', "value": "62bfef07e4b0b34d0df15ebb"}, {"domain": "www.yunzhijia.com", "expiry": 1667212204, "httpOnly": 'false', "name": "qimo_seokeywords_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02", "path": "/", "secure": 'false', "value": ""}, {"domain": "www.yunzhijia.com", "expiry": 1667212204, "httpOnly": 'false', "name": "qimo_seosource_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02", "path": "/", "secure": 'false', "value": "%E7%AB%99%E5%86%85"}, {"domain": ".yunzhijia.com", "httpOnly": 'true', "name": "redirectIndexUrl", "path": "/", "secure": 'false', "value": "/cloud-office/pc/index.html"}, {"domain": ".yunzhijia.com", "httpOnly": 'true', "name": "uuid", "path": "/", "secure": 'false', "value": "725d8ca0-06ca-4492-a69b-19ba38bbc909"}, {"domain": "www.yunzhijia.com", "expiry": 1667212204, "httpOnly": 'false', "name": "qimo_seokeywords_0", "path": "/", "secure": 'false', "value": ""}, {"domain": ".yunzhijia.com", "expiry": 1698746404, "httpOnly": 'false', "name": "Hm_lvt_a96914087b350d1aa86c96cdbf56d5e5", "path": "/", "secure": 'false', "value": "1667210405"}, {"domain": "www.yunzhijia.com", "httpOnly": 'false', "name": "href", "path": "/", "secure": 'false', "value": "https%3A%2F%2Fwww.yunzhijia.com%2Fhome%2F%3Fm%3Dopen%26a%3Dlogin%26utm_source%3D%26utm_medium%3D"}, {"domain": ".yunzhijia.com", "httpOnly": 'true', "name": "__att_token", "path": "/", "secure": 'false', "value": "fDyIdtU1ryZNzZeOX93EwTnLfBmfxN2G"}, {"domain": "www.yunzhijia.com", "expiry": 1667212204, "httpOnly": 'false', "name": "qimo_xstKeywords_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02", "path": "/", "secure": 'false', "value": ""}, {"domain": "www.yunzhijia.com", "httpOnly": 'true', "name": "cd", "path": "/", "sameSite": "None", "secure": 'true', "value": "yunzhijia.com"}, {"domain": "www.yunzhijia.com", "expiry": 1667296804, "httpOnly": 'false', "name": "uuid_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02", "path": "/", "secure": 'false', "value": "b57d54bb-f115-4c98-a8e0-bb75e145626f"}, {"domain": "www.yunzhijia.com", "httpOnly": 'true', "name": "cu", "path": "/", "sameSite": "None", "secure": 'true', "value": "62bfef07e4b0b34d0df15ebb"}, {"domain": "www.yunzhijia.com", "expiry": 1667296804, "httpOnly": 'false', "name": "accessId", "path": "/", "secure": 'false', "value": "ce3d5ef0-6836-11e6-85a2-2d5b0666fd02"}, {"domain": "www.yunzhijia.com", "expiry": 1667212204, "httpOnly": 'false', "name": "qimo_seosource_0", "path": "/", "secure": 'false', "value": "%E7%AB%99%E5%86%85"}, {"domain": "www.yunzhijia.com", "expiry": 1667296804, "httpOnly": 'false', "name": "pageViewNum", "path": "/", "secure": 'false', "value": "1"}]
data_url = 'https://www.yunzhijia.com/attendance/rest/web-record/clockIns?userId=62bfef07e4b0b34d0df15ebb&qryDate='+'2022-11-1'
se = requests.session()
headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'referer': 'https://www.yunzhijia.com/attendance-web/myAttendance',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0', 
    'sec-ch-ua-platform': 'Windows', 
    'sec-fetch-dest': 'empty', 
    'sec-fetch-mode': 'cors', 
    'sec-fetch-site': 'same-origin', 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

for cookie in listCookies:
    se.cookies.set(cookie['name'], cookie['value'])

response =  se.get(url=data_url, headers=headers)

clockInResult =  response.json()

clockInResultlength = len(clockInResult['data'])

print(clockInResult)
print(clockInResultlength)
print(type(clockInResultlength))
        