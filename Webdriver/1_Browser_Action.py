from  selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
# driver=webdriver.Chrome()
# driver=webdriver.Ie()

driver.get("http://www.51zxw.net")
print(driver.title)
driver.maximize_window()
sleep(2)

driver.get("http://www.51zxw.net/list.aspx?cid=615")
driver.set_window_size(400,800)
driver.refresh()
sleep(2)

driver.back()
sleep(2)

driver.forward()
sleep(2)

driver.quit()