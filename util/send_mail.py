#coding = utf-8import smtpdimport smtplibfrom email.mime.text import MIMETextfrom email.header import Headerclass SendMail:    def __init__(self, mail_host):        self.mail_host = mail_host    def send(self, title, content, sender, auto_code, receivers):        message = MIMEText(content, 'html', 'utf-8')        message['From'] = '{}'.format(sender)        message['To'] = ','.join(receivers)        message['Subject'] = title        try:            smtp_obj = smtplib.SMTP_SSL(self.mail_host, 465)#启动ssl发信，端口一般是465            smtp_obj.login(sender, auto_code)#授权码            smtp_obj.sendmail(sender, receivers, message.as_string())            print('Mail 发送成功')        except Exception as e:            print(e)if __name__ == '__main__':    mail = SendMail('smtp.126.com')    sender = 'tydragon_tian@126.com'    receivers = ['yunlong.tian@ezhiyang.com']    title = '自动化测试报告'    content = '''        小滴课堂  xdclass.net        <a href = 'https://xdclass.net'>进入学习课堂</a>    '''    auto_code = 'KUEXTZPLUGJHEURU'    mail.send(title, content, sender, auto_code, receivers)