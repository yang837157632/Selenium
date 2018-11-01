from  selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")

driver.find_element_by_css_selector("#kw").send_keys("Python")
sleep(2)

#全选
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
sleep(2)

#复制或者剪切
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')
driver.get("http://www.sogou.com/")
sleep(2)

#粘贴关键词
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL,'v')
sleep(2)

driver.find_element_by_css_selector("#stb").click()
sleep(4)

driver.quit()


