import os,shutil
import time
import os_file
import logging
import re



#src_path='D:/新建文件夹/WeChat Files/ramchan1988/FileStorage/File/2020-06/'
src_path='E:/HUMEI/核价/'
target_path='E:/HUMEI/核价/'
txt="我要查税金"
def run(src_path,target_path,txt):
    file_list=os.listdir(target_path)
    if len(file_list)>0:
        for file in file_list:
            logging.info(file)


    all_file = os_file.open(self=src_path, all=1)
    if len(all_file) > 0:
        for per_file in all_file:
            #logging.info(per_file)
            if txt in per_file:
                logging.info("OK  "+str(per_file))

                filename=re.findall(r"/2020-07/(.*)",str(per_file))
                #logging.info(filename)
                shutil.move(str(per_file), target_path  +filename[0])


    else:
        logging.info("文件夹是空的")

    #return "move"



if __name__ == '__main__':
    # logging.info("dd")
    run(src_path,target_path,txt)

"""
while True:
    time.sleep(3)
    file_list=os.listdir(target_path)
    if len(file_list)>0:
        for file in file_list:
            logging.info(file)
            #shutil.move(src_path+file,target_path+file)
"""