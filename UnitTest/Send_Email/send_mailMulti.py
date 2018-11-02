import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.qq.com'

sender='837157632@qq.com'
receives=['1446806744@qq.com','ymin@hpe.com']

user=sender
password='...'

subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=','.join(receives)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msg.as_string())
smtp.quit()
print("Send email end!")