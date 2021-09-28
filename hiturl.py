from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
#driver = webdriver.Chrome('C:/Users/Seb/PycharmProjects/pythonProjectTinBo/chromedriver_win32 (1)/chromedriver.exe')
from random import seed
from random import random
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from soup import Get_soup
# from secrets import username, password

global driver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument('headless')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('???')
chrome_options.add_argument('--no-proxy-server')


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://getpocket.com/my-list/tags')
driver.maximize_window()
a=[]
# send_keys(addresss)
def Login():
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[1]/input').send_keys('alexboone29@gmail.com')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[2]/input').send_keys('0qxKPZnNqCdf')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[2]/input').send_keys(Keys.ENTER)
    time.sleep(10)
    el=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/nav/button[10]')
    driver.execute_script("arguments[0].click();", el)         # clicking on all tags button
    time.sleep(5)
    alltages=driver.find_elements_by_class_name('p1mk9fki')   # find all tages return a list
    # a.append(alltages)
    for i in alltages:
        a.append('https://getpocket.com/my-list/tags/'+(i.text))
        # el=a[0][i]
        # driver.execute_script("arguments[0].click();", el)
        # time.sleep(5)
    for i in range (1,2):
        driver.get(a[i])    
        time.sleep(10) 
        res=driver.page_source
        soup=BeautifulSoup(res,'html.parser')
        all_links=soup.find_all('a',{'data-cy':'title-link'})
        links_list=[]
        for li in all_links:
            # links_list.append("https://getpocket.com"+i.get('href'))
            
                driver.get("https://getpocket.com"+li.get('href'))    
                time.sleep(10)
                res=driver.page_source
                soup=BeautifulSoup(res,'html.parser')
                Get_soup(soup,li)
              
               
        all_links.clear()
            
        # driver.get('https://getpocket.com/my-list/tags')

        # time.sleep(10)

    
    

