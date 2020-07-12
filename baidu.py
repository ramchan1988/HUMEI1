# -*- coding: utf-8 -*-
"""
发送邮件和附件
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import re
import logging

# ------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),
# ------------------------------



def send(per_file):
    #logging.info(per_file)
    fromaddr = '171807653@qq.com'
    #password = 'UHWEHDHKZTBDPIAK'
    password = 'wueacihsuvbvbifa'

    toaddrs = ['171807653@qq.com', '171807653@qq.com']
    filename = re.findall(r"/转发1/(.*)", str(per_file))
    #logging.info(filename[0])
    logging.info( 'filename=%s'%filename[0])

    textApart = MIMEMultipart()
    #att1 = MIMEApplication(open('E:/HUMEI/Excel_shunxu/税金1/1.txt', 'rb').read())
    att1 = MIMEApplication(open(per_file, 'rb').read())
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=%s'%filename[0]
    textApart.attach(att1)

    textApart['From'] = fromaddr
    textApart['To'] = fromaddr

    send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    subject = '邮件测试' + send_time
    textApart['Subject'] = subject

    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, textApart.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误






