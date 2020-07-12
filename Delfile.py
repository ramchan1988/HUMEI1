"""
清空文件夹内的文件
"""

import os
import os_file


ADD = "E:/HUMEI/Excel_shunxu/检测1/"
def delfile(ADD):

    all_file = os_file.open(self=ADD, all=1)
    #print("正在分析", all_file)
    for per_file in all_file:
        #print(per_file)
        os.remove(per_file)
