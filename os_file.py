import os
import logging
"""
读取文件函数
"""
# ------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="\033[37m[%(asctime)s] [%(pathname)s] (%(levelname)s-第%(lineno)d行) \n%(message)s\033[0m")

# ------------------------------



def open(self, all):  # 读取文件夹内文件  # 输入路径
    """
    :param self: 文件夹的路径
    :param all: all==0:是xls文件;all==1:是所有文件
    :return:输出所有文件名的列表
    """
    try:

        file_list = os.walk(self)
        #print(file_list)
        path_list=[]
        count = 0
        for ph in file_list:
            #print(ph)
            ph[0]==self
            path_list = ph[2]

            break
            #count += len(path_list)   # 计数器

        while len(path_list) == 0:
            raise Exception("错误路径或者该文件夹为空")

        a = []
        n = 0
        for e in path_list:
            if all == 1:
                # print("读取文件", '%s' % n, e)
                e = self + e
                a.append(e)

            if all == 0 and ".xls" in e:
                # print("读取文件", '%s' % n, e)
                e = self + e
                a.append(e)




            n = n + 1

        return a



    except Exception as e:
        raise
        #raise e("The folder is empty")
        logging.info(e)
        print("Path error")
        return []


if __name__ == '__main__':
    a=open('E:/HUMEI/核价/',all=1)
    print(a)








