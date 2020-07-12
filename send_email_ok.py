# -*- coding: utf-8 -*-
"""
  压缩文件并发邮件
"""
import os_file
import logging
import baidu
import time
import zipfile
import os
# ------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),
# ------------------------------



def run(ADD):
    # ADD = "E:/HUMEI/Excel_shunxu/转发1/"

    all_file = os_file.open(self=ADD, all=1)
    #print("正在分析", all_file)


    if len(all_file) > 0:  # 判断是否有文件
        zip = zipfile.ZipFile(ADD + "file.zip", "w", zipfile.ZIP_DEFLATED)
        p = 0
        for per_file in all_file:
            logging.info(per_file)
            zip.write(per_file)
            logging.info(zip.write(per_file))


            #time.sleep(5)
            logging.info("%s is OK"%per_file)
    #else:
        #logging.info("不存在文件")
    zip.close()
    baidu.send(ADD + "file.zip")



if __name__ == '__main__':
    ADD = "E:/HUMEI/Excel_shunxu/转发1/"
    run(ADD)
