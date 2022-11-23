
from email import message
from selenium.webdriver.common.by import By
from selenium import webdriver
from PIL import Image
import pytesseract
import schedule
import requests
import logging
import time
import os

def main(name, passwd):
    network_status = False
    i = 1 
    # 循环连接网络
    while not network_status:
        # 1. 测试网络连接状态,如果已经连接网络，就退出循环
        network_status = test_network_status()
        if network_status:
            break
        logging.info('进行第{}次连接'.format(i))
        connect_network(name, passwd)
        time.sleep(10)
        i+=1
        if i > 10:
            return
    logging.info("网络已连接")
    return True
    
def test_network_status():
    """测试当前电脑是否有网

    Returns:
        _type_: boolean
    """
    try:
        request = requests.get('https://www.baidu.com/',timeout=1)
        if request.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        logging.info(e)
        return False

    # os.system('chcp 65001') 
    # network_status=os.system('ping -n 2 -w 1 www.baidu.com')
    # print(network_status)
    # return network_status

def connect_network(name, passwd):
    """连接网络

    Args:
        name (_type_): 账户
        passwd (_type_): 密码

    Returns:
        _type_: boolean
    """
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        # 创建Chrome浏览器对象
        browser = webdriver.Chrome(options=option)
        #访问百度网站
        browser.get('http://192.168.2.253:7755/login.cgi?s=192.168.2.253&p=5280&auths=192.168.2.253&authp=7755&authmethod=1')
        # 查找所有运算
        inputusername = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input").send_keys(name)
        inputpasswd = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input").send_keys(passwd)
        # imgsrc = browser.find_element('css selector', 'img')
        imgsrc = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/img").get_attribute('src')

        img_path = 'yzm.png'

        # 通过requests.get获得图片
        r=requests.get(imgsrc)
        r.raise_for_status()
        # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
        with open(img_path,'wb') as f:
            f.write(r.content)
            f.close()

        yzm_value = proc_img(img_path)
        if yzm_value:
            browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input").send_keys(yzm_value)
            wsubmit = browser.find_element(by=By.XPATH, value="/html/body/form/table[4]/tbody/tr/td[2]/table/tbody/tr[5]/td/input")
            time.sleep(2)
            wsubmit.click()
            time.sleep(2)
    except Exception as e:
        logging.info(e)
        return False
    finally:
        time.sleep(2)
        # 关闭浏览器
        browser.close()
    return True
    
    
def proc_img(img_path):
    def calc_diff(pixel):
        """处理图片，去除验证码中除数字以外的杂色

        Args:
            pixel (_type_): 颜色RGB值

        Returns:
            _type_: str
        """
        if pixel[0] == 200 and pixel[2] == 200 and pixel[2] == 200:
            return False
        # if pixel[0] == 175 or pixel[1] == 75 or pixel[2] == 125:
        #     return False
        if pixel[0] != pixel[2]   and pixel[1] != pixel[2]:
            if pixel[0] >  50   or pixel[1] > 50 or  pixel[2] > 50:
                return False
        return True

    im  = Image.open(img_path).convert(mode='RGB')
    delete_color = [237, 237, 237]
    pixdata = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            if not calc_diff(pixdata[x, y]):
                pixdata[x, y] = (255, 255, 255)     
    im.save("output1.png")

    config = r'--oem 3 --psm 6 outputbase digits'
    result = pytesseract.image_to_string(Image.open('output1.png'), config=config)
    os.remove('output1.png')
    os.remove(img_path)
    return result

if __name__ == '__main__':
    """
        自动连接网络
    """
    logging.basicConfig(filename="./connectLog.txt",level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    name = '韩成城'
    passwd = '123456'
    schedule.every(10).minutes.do(main,name=name,passwd=passwd)
    while True:
        schedule.run_pending()
        time.sleep(5)
