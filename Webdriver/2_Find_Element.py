from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.find_element_by_class_name("s_ipt").send_keys("Selenium")
sleep(2)

driver.get("http://www.baidu.com")
driver.find_element_by_name("wd").send_keys("Selenium我要自学网")
sleep(2)

driver.get("http://www.51zxw.net")
# driver.find_element_by_tag_name("input").send_keys("Selenium")
driver.find_elements_by_tag_name("input")[1].send_keys("Selenium")
sleep(2)

driver.get("http://www.51zxw.net")
driver.find_element_by_link_text("程序开发").click()
sleep(2)
driver.find_element_by_partial_link_text("神秘面纱").click()
sleep(2)

driver.find_element_by_id("su").click()
sleep(2)

driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("Selenium 我要自学网")
driver.find_element_by_css_selector(".s_ipt").send_keys("Selenium")
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("Python3")
sleep(2)

driver.get("http://www.51zxw.net")
driver.find_element_by_css_selector("form#loginForm>ul>input[type='password']").send_keys('51zxw666')
sleep(2)

driver.quit()