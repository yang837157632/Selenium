from  selenium import webdriver
from time import sleep
import os

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")

driver.find_element_by_css_selector(".soutu-btn").click()
sleep(2)

driver.find_element_by_css_selector(".upload-pic").send_keys(os.path.join(os.getcwd(), "shuiyin.png"))
sleep(3)

driver.quit()
