import smtplib
from email.mime.text import MIMEText
from email.header import Header

#收件人
sender = "yunlong.tian@ezhiyang.com"
receiver = "65885387@qq.com"

#授权码 eJAuqQYcU4Q7vk8r
auth_code = "eJAuqQYcU4Q7vk8r"

#主题
subject = "自动化测试报告"

#定义发送内容
msg = MIMEText("<html> <h2>欢迎来到自动化测试</h2></html>", _subtype="html", _charset="utf-8")
msg["Subject"] = subject
msg["from"] = sender
msg["to"] = receiver

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login(sender, auth_code)

smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()