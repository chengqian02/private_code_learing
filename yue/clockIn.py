from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from interval import Interval
import schedule
import requests
import logging
import time
import json

class getDailySigninfo:
    def __init__(self, token, topic) -> None:
        # self.headers = {
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        #     }
        self.headers = {
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
        self.headers_baidu = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'www.baidu.com',
            'referer': 'http://www.baidu.com/',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0', 
            'sec-ch-ua-platform': 'Windows', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors', 
            'sec-fetch-site': 'same-origin', 
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
            }
        self.listCookies = []
        self.cookiesFileName = 'cookies.txt'
        self.token = token
        self.topic = topic

    def getCookie(self):
        try:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            option.add_argument('blink-settings=imagesEnabled=false')
            # 创建Chrome浏览器对象
            browser = webdriver.Chrome(options=option)
            # browser = webdriver.Chrome()
            url = 'https://www.yunzhijia.com/home/?m=open&a=login&utm_source=&utm_medium='
            browser.get(url)
            time.sleep(3)
            browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[2]/div/div/h3/div[2]").click()
            time.sleep(1)
            browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[2]/div/div/div[1]/form/div[1]/input").send_keys('13293785075')
            time.sleep(1)
            browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[2]/div/div/div[1]/form/div[2]/input[1]").send_keys('Sy123123')
            time.sleep(3)
            browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[2]/div/div/div[1]/form/div[2]/input[3]").send_keys(Keys.ENTER)
            time.sleep(5)
            ActionChains(browser).move_to_element(browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/span")).perform()
            time.sleep(1)
            browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/div/ul/li[1]/a").click()
            time.sleep(30)
            ActionChains(browser).move_to_element(browser.find_element(by=By.XPATH, value="/html/body/header/div[2]/div/div[2]/ul/li[3]")).perform()
            time.sleep(5)
            browser.find_element(by=By.XPATH, value="/html/body/header/div[2]/div/div[2]/ul/li[3]/div/div[1]/div[1]").click()
            time.sleep(30)
        except Exception as e:
            logging.info(e)
        finally:
            ListCookies = browser.get_cookies()  
            jsonCookies = json.dumps(ListCookies) # 转换成字符串保存
            logging.info("保存cookies")
            logging.info("cookies是：{}".format(jsonCookies))
            with open(self.cookiesFileName, 'w') as f:
                f.write(jsonCookies)
            logging.info("cookies保存成功！")
            browser.quit()
        return True

    def getDailySigninfo(self, currentTime):
        i = 0
        logging.info("从文件中读取cookies，并请求打卡数据")
        response=[]
        if not self.get_json_data(currentTime, response):
            return False
        # response =se.get(url=self.data_url, headers=self.headers)
        responseR =response.pop()
        while responseR.json()['code'] != 200:
            if i > 2:
                return False
            logging.info("获取到的数据错误：{}".format(responseR))
            logging.info("cookies失效，重新获取cookie")
            if not self.getCookie():
                return False
            logging.info("从文件中读取cookies，并请求打卡数据")
            if not self.get_json_data(currentTime, response):
                return False
            responseR =response.pop()
            
        logging.info("获取打卡数据成功")
        return responseR.json()

    def get_json_data(self, currentTime, response):
        try:
            if not self.test_network_status():
                return False
            data_url = 'https://www.yunzhijia.com/attendance/rest/web-record/clockIns?userId=62bfef07e4b0b34d0df15ebb&qryDate='+currentTime.split(" ")[0]
            # data_url = 'https://www.yunzhijia.com/attendance/rest/web-record/clockIns?userId=62bfef07e4b0b34d0df15ebb&qryDate='+'2022-11-04'
            se = requests.session()
            with open(self.cookiesFileName, 'r', encoding='utf8') as f:
                self.listCookies = json.loads(f.read())
            for cookie in self.listCookies:
                se.cookies.set(cookie['name'], cookie['value'])
            logging.info('请求数据的url：{}'.format(data_url))
            response.append(se.get(url=data_url, headers=self.headers))
        except Exception as e:
            logging.info(e)
            return False
        finally:
            se.close()
        return True


    def sendWeiXinMessage(self, title, msg):
        try:
            token = self.token
            title =title
            content = msg
            template = 'html'
            topic = self.topic
            url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}&topic={topic}"
            logging.info('发送消息的url：{}'.format(url))
            r = requests.get(url=url)
        finally:
            r.close()
            return json.loads(r.text)


        
    def test_network_status(self):
        """测试当前电脑是否有网

        Returns:
            _type_: boolean
        """
        try:
            # request = requests.get('http://www.baidu.com/', headers=self.headers_baidu)
            request = requests.get('http://www.baidu.com')
            if request.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            logging.info(e)
            return False
        finally:
            request.close()

    # 输入毫秒级的时间，转出正常格式的时间
    def timeStamp(self, timeNum):
        timeStamp = float(timeNum/1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%H:%M:%S", timeArray)
        return otherStyleTime

    # 判断当前时间是否在某时间范围内
    def judge_time(self, currentTime , time_interval_one, time_interval_two):
        if currentTime in Interval(time_interval_one, time_interval_two):
            return True
        return False

    # 判断获取的信息中是否有某时间段
    def judge_cloclInTime(self,clockInResult, time_interval_one, time_interval_two):
        clockInData = clockInResult['data']
        if len(clockInData) == 0:
            return False
        for clockIn in clockInData:
            clockInTimeTemp = float(clockIn['clockInTime'])
            clockInTime =  self.timeStamp(clockInTimeTemp)
            if self.judge_time(clockInTime , time_interval_one, time_interval_two):
                return True
        return False

    def main(self):
        i = 1
        j = 2
        logging.info("开始检测打卡行为")
        while True:
            logging.info("第{}次获取打卡信息".format(i))
            currentTime = time.strftime('%Y-%m-%d %S:%H:%M',time.localtime(time.time()))
            hour = int(currentTime.split(":")[1])
            minute = int(currentTime.split(":")[2])
            if (hour != 6 and hour != 7 and hour !=11 and hour != 12 and hour != 13 and hour != 18):
                logging.info("不在需要检测的时间范围")
                return
            clockInResult = self.getDailySigninfo(currentTime)
            if not clockInResult:
                logging.info("cookies失效，请检查程序")
                time.sleep(1*60)
                continue
            clockInResultlength = 0
            clockInResultlength = len(clockInResult['data'])
            logging.info("获取到的打卡数据{}".format(clockInResult))
            logging.info("当前时间{} {}:{},今天已经打了{}次卡".format(currentTime.split(" ")[0], hour, minute, clockInResultlength))
            currentTime = time.strftime('%H:%M:%S',time.localtime(time.time()))
            minute = int(currentTime.split(":")[1])
            if self.judge_time(currentTime, "06:30:00", "07:30:00"):
                if self.judge_cloclInTime(clockInResult, "06:30:00", "07:30:00"):
                    title = '打卡成功,早上好, 记得去吃早饭'
                    msg = '悦，早上好，记得吃早饭'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("打卡成功，发送信息成功")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))
                    return True
                else:
                    title = '没有打卡通知'
                    msg = '悦，该打卡了，还剩余'+(str(60-minute+30) if minute > 30 else str(30 - minute))+'分钟，打了卡去吃早饭'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("发送消息，重行获取打卡信息")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))
                        
            if self.judge_time(currentTime, "11:30:00", "12:30:00"):
                if self.judge_cloclInTime(clockInResult, "11:30:00", "12:30:00"):
                    title = '打卡成功，去吃饭吧'
                    msg = '如果中午没事做就和我聊天吧'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("打卡成功，发送信息成功")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))
                    return True
                else:
                    title = '没有打卡通知'
                    msg = '悦，该打卡了，还剩余'+(str(60-minute+30) if minute > 30 else str(30 - minute))+'分钟，打了卡去吃饭'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("发送消息，重行获取打卡信息")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))

            if self.judge_time(currentTime, "13:00:00", "14:00:00"):
                if self.judge_cloclInTime(clockInResult, "13:00:00", "14:00:00"):
                    title = '打卡成功，午安'
                    msg = '午安！'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("打卡成功，发送信息成功，退出程序")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))
                    return True
                else:
                    title = '没有打卡通知'
                    msg = '悦，该打卡了，还剩余'+str(60-minute)+'分钟,打完卡睡觉'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("发送消息，重行获取打卡信息")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))
                    j = j+1
            
            if self.judge_time(currentTime, "18:00:00", "19:00:00"):
                if self.judge_cloclInTime(clockInResult, "18:00:00", "19:00:00"):
                    title = '打卡成功'
                    msg = '悦，好好吃晚饭，给你+1'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("打卡成功，发送信息成功，退出程序")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))
                    return True
                else:
                    title = '没有打卡通知'
                    msg = '悦，该打卡了，还剩余'+str(60-minute)+'分钟'
                    messageResult = self.sendWeiXinMessage(title, msg)
                    if messageResult['code'] == 200:
                        logging.info("发送消息，重行获取打卡信息")
                    else:
                        logging.info("发送消息失败，原因：{}".format(messageResult['msg']))

            logging.info("等待获取新的打卡信息")
            if j > 2:
                time.sleep(47*60)
                j = 0
            else:
                time.sleep(5*60)
            i=i+1
            if i>13:
                return False
            


if __name__ == '__main__':
    # token
    logging.basicConfig(filename="./clockInLog.txt",level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("程序开始")
    token = '067bb93e90c942ae8cc984622fbed7a7'
    topic = 'daka'
    logging.info("初始化基础信息")
    getDailySigninfo = getDailySigninfo(token=token, topic=topic)
    # 定时调度程序
    schedule.every().day.at("07:04").do(getDailySigninfo.main)
    schedule.every().day.at("11:30").do(getDailySigninfo.main)
    schedule.every().day.at("13:03").do(getDailySigninfo.main)
    schedule.every().day.at("18:00").do(getDailySigninfo.main)
    logging.info("运行调度程序")
    while True:
        schedule.run_pending()
        time.sleep(5)

    # 调试入口
    # getDailySigninfo.main()