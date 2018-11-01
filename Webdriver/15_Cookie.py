from selenium import webdriver
from  time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/")

cookie=driver.get_cookies()
print(cookie)
print(cookie[0])

driver.add_cookie({'name':'51zxw','value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print("%s——%s" %(cookie['name'],cookie['value']))


# 基于Cookie绕过验证码自动登录
#手动添加cookie
driver.get("http://www.baidu.com/")
driver.add_cookie({'name':'BAIDUID','value':'9E4BF1D44014…(根据实际获取值填写)'})
driver.add_cookie({'name':'BDUSS','value':'根据实际抓包获取值填写'})
sleep(2)

driver.refresh()
sleep(3)

driver.quit()
