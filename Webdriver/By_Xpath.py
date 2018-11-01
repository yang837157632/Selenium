from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
sleep(2)
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("Selenium")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("51zxw")
# driver.find_element_by_xpath("//input[@name='wd']").send_keys("51zxw")
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Python")
sleep(2)

driver.find_element_by_id('su').click()
sleep(2)

driver.get("http://www.51zxw.net/")
sleep(3)

#层级定位
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys('51zxw')
#组合定位
driver.find_element_by_xpath("//input[@class='loinp' and @name='username']").send_keys('51zxw')
sleep(2)

driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys(6666)
sleep(2)

driver.quit()