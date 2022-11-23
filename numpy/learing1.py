# 导入seleinum webdriver接口
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import requests

import time
def sign_user():
    # 创建Chrome浏览器对象
    browser = webdriver.Chrome()
    #访问百度网站
    browser.get('http://192.168.2.253:7755/login.cgi?s=192.168.2.253&p=5280&auths=192.168.2.253&authp=7755&authmethod=1')



    # 查找所有运算
    inputusername = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input").send_keys('韩成城')
    inputpasswd = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input").send_keys('123456')
    imgsrc = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/img").get_attribute('src')
    
    path = 'yzm.png'

    # 通过requests.get获得图片
    r=requests.get(imgsrc)
    r.raise_for_status()
    # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("保存成功")
    time.sleep(0.5)
    verCode = verCodeOcr()
    imgInput = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input").send_keys(verCode)
    wsubmit = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[5]/td/input")
    wsubmit.click()
    input("sjdk")
    
def verCodeOcr():
    # 英文识别
    filename = 'yzm.png'
    img = Image.open(filename)
    result = pytesseract.image_to_string(img, lang='eng')
    result = result.replace('\n','').replace(' ','')
    print(f'英文识别结果：\n {result}')
    return result
    
if __name__=="__main__":
    sign_user()
    verCodeOcr()







