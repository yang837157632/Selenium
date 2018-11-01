from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
file_path=r"Frame.html"
driver.get(file_path)
sleep(2)

driver.switch_to.frame("search")
driver.find_element_by_css_selector("#query").send_keys("Python")
sleep(2)

driver.find_element_by_css_selector("#stb")
sleep(2)

driver.quit()