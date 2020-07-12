import os_file
import xlrd
from xlutils.copy import copy as xl_copy
import os
import logging
"""
xls格式转xlsx
"""


def formast(ADD):
    all_file = os_file.open(self=ADD, all=1)
    try:
        for per_file in all_file:
            if per_file[-4:] == ".xls":
                rb = xlrd.open_workbook(filename=per_file)
                wb = xl_copy(rb)
                wb.save(per_file + "x")
                logging.info(per_file+"--转换成功")
                os.remove(per_file)
    except Exception as e:
        raise e





if __name__ == '__main__':
    ADD = "E:/HUMEI/Excel_shunxu/检测/"
    formast(ADD)
