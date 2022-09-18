# -*- coding: utf-8 -*-

#Import libraries:

import requests
from time import sleep
from selenium import webdriver
import chromedriver_binary

#Here we use selenium to send base request for getting cookie:

driver = webdriver.Chrome()
sleep(5)
driver.maximize_window()
sleep(5)
driver.get("https://www.linkedin.com/")
sleep(5)

#Save cookie in variable:

cookies_dict = {}
for cookie in driver.get_cookies():
        cookies_dict[cookie['name']] = cookie['value']
        
driver.close()

#Set headers & Send a get request:

resp = requests.get("https://www.linkedin.com/in/aniesh-das-aa0a40204/",
                     cookies=cookies_dict,
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                                   'accept-encoding': 'gzip, deflate, br',
                                                   'accept-language': 'en-US,en;q=0.9',
                                                   'upgrade-insecure-requests': '1',
                                                   'scheme': 'https'})
        
html = resp.text

#Save Profile page in Local Folder:

HtmlPath = "E:/user/Desktop/BE college/Extra Python projects/web scraper/1.html"
page_fun = open(HtmlPath,'w',encoding='utf-8')
page_fun.write(html)
page_fun.close()