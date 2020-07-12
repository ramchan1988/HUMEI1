import logging
'''
列表合并成一个字符串
'''
logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),

def tostr(self):

    if type(self) == list:
        #print("OK")
        s = ""
        #logging.info("OK")
        for i in self:
            #logging.info(i)
            s=s+str(i)+"<br>"
        #logging.info(s)
        return s
    else:
        logging.info("错误")
        return ""





