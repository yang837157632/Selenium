import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

smtpserver='smtp.qq.com'

sender='837157632@qq.com'
receives=['1446806744@qq.com','ymin@hpe.com']

user=sender
password='...'


subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

filepath=os.path.join(os.getcwd(), "Selenium.png")
send_file=open(filepath,'rb').read()

att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="Selenium.png"'


msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print("Send email end!")



