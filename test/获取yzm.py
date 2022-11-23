
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import requests
from operator import mod
import re
import time
import os
import re

# p = subprocess.Popen(["ping.exe ", 'www.baidu.com '],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True)

# out = p.stdout.read()

# print(out)

# regex = re.compile("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", re.IGNORECASE)

# print(regex.findall(out))

# import os
# os.system('chcp 65001') 
# return1=os.system('ping -n 2 -w 1 www.baidu.com')

# print(return1)

def connect_network(path):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    # 创建Chrome浏览器对象
    browser = webdriver.Chrome(options=option)
    #访问百度网站
    browser.get('http://192.168.2.253:7755/login.cgi?s=192.168.2.253&p=5280&auths=192.168.2.253&authp=7755&authmethod=1')
    # 查找所有运算
    inputusername = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input").send_keys('韩成城')
    inputpasswd = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input").send_keys('123456')
    # imgsrc = browser.find_element('css selector', 'img')
    imgsrc = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/img").get_attribute('src')

    

    # 通过requests.get获得图片
    r=requests.get(imgsrc)
    r.raise_for_status()
    # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("保存成功")
  
for i in range(10):
    path = 'E:\\code\\python\\images\\'+str(i)+'.png'
    connect_network(path)