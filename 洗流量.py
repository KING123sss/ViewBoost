from selenium import webdriver
import time
import random
import requests
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('headless')
user_agent = UserAgent()

with open('proxy_list.txt', 'r') as file:
    proxy_ips = file.read().splitlines()
    
s=Service(r"D:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

  
for i in range(100):
     try:
        proxy_ip = random.choice(proxy_ips)  # 隨機取得Proxy IP
        print(f'使用的Proxy IP：{proxy_ip}')
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
        "Host": "https://www.youtube.com/watch?v=ULCZotw-ank",  # 目標網站
        "Referer": "https://www.youtube.com/",  # 參照位址
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-site",
        "Content-Length":'0',
        "Connection":"keep-alive"
        }
        driver.get('https://www.youtube.com/watch?v=ULCZotw-ank') # 目標網站
        response = requests.get(url="https://youtu.be/ULCZotw-ank",headers={ 'user-agent': user_agent.random })
        print("response for {} time".format(i))
        delay_choices = [60, 61, 62, 63, 64, 65]  # 延遲的秒數
        delay = random.choice(delay_choices)  # 隨機選取秒數
        time.sleep(delay)  # 延遲
        
        
     except:
          print('爬蟲發生錯誤!')

driver.close()

