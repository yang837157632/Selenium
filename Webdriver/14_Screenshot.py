from  selenium  import webdriver
from  time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/")
driver.get_screenshot_as_file("51zxw.jpg")
sleep(2)

driver.get("http://www.baidu.com/")
driver.get_screenshot_as_file(r"baidu.png")
sleep(2)

driver.quit()