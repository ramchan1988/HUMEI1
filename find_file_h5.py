# -*- coding: utf-8 -*-

'''
检查获取的文件 用于web上面
'''


import os_file
import logging
import re

# ------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="\037[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\037[0m"),

# ------------------------------

def run(src_path,txt):
    all_file = os_file.open(self=src_path, all=1)
    if len(all_file) > 0:
        s=""
        for per_file in all_file:
            #logging.info(per_file)
            if txt in per_file:
                logging.info("OK  "+str(per_file))
                filename=re.findall(r"/2020-07/(.*)",str(per_file))
                logging.info(type(filename))
                s=s+filename[0]+"<br>"
                #logging.info(s)

    if s=="":
        logging.info("找不到文件")
        return "找不到文件 请通过微信发送文件"
    else:
        logging.info(s)
        return s













if __name__ == '__main__':
    src_path = 'D:/新建文件夹/WeChat Files/ramchan1988/FileStorage/File/2020-06/'
    txt = "我要查税金"
    run(src_path,txt)