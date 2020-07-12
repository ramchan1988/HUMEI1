import xlrd, xlwt
from xlutils.copy import copy as xl_copy
import os_file
import openpyxl

"""
新建一个工作页
"""
def New_Sheet(ADD, sheetname):
    """
    :param add: 地址
    :param sheetname: 工作页的命名
    :return:
    """
    all_file = os_file.open(self=ADD, all=1)
    for per_file in all_file:
        print("分析结果", per_file)


        rb = xlrd.open_workbook(filename=per_file)
        wb = xl_copy(rb)
        wb.add_sheet(sheetname=sheetname)
        wb.save(per_file+"x")

        print('succeed')










if __name__ == '__main__':
    ADD = "E:/HUMEI/Excel_shunxu/检测1/"
    New_Sheet(ADD,sheetname="43")