import os_file
import OpenExcel
import DataSum
import NewSheet
import RowData
import xlrd, xlwt
from xlutils.copy import copy as xl_copy
import datetime
import re
import logging


def build_waybill():
    ADD = "E:/HUMEI/Excel_shunxu/检测1/"
    ADD_none = r"E:\HUMEI\Excel_shunxu\空表\none.xls"
    ADD_waybill = "E:/HUMEI/Excel_shunxu/顺序模板/waybill_0.xlsx"

    all_file = os_file.open(self=ADD, all=1)
    #print("正在分析", all_file)
    row_waybill = OpenExcel.open_excel_row(ADD_waybill, sheet=0, row=0)
    #print("row_waybill", row_waybill)
    logging.info("生成运单OK")

    p = 0
    for per_file in all_file:

        #print("waybill.py", p, per_file)

        # workbook = xlrd.open_workbook(filename=per_file)
        workbook_none = xlrd.open_workbook(filename=ADD_none)
        wb = xl_copy(workbook_none)
        # wb.add_sheet("waybill")

        try:
            s = wb.get_sheet(0)


        except:
            print("错误：请新建Sheet")

        sheet_0 = OpenExcel.open_excel_sheet(per_file, sheet=0)
        row_1 = OpenExcel.open_excel_row(per_file, sheet=0, row=0)
        #print(row_1)

        for i in range(23):

            a = 0
            for x in RowData.row_name(row_waybill[i], row_1, sheet_0):
                s.write(a, i, x)
                a = a + 1
        new_name = re.findall("/检测1/(.+)_20", per_file)
        #print(new_name)
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d_%H：%M：%S')
        #print(nowTime)
        p = p + 1
        wb.save("E:/HUMEI/Excel_shunxu/检测3/" + "%s waybill_%s.xls" % (new_name[0], p))
        # wb.save("E:/HUMEI/Excel_shunxu/检测3/" + "%s.xls" % new_name)
        wb.save("E:/HUMEI/Excel_shunxu/转发1/" + "%s waybill_%s.xls" % (new_name[0], p))




if __name__ == '__main__':
    build_waybill()
    print('succeed in buliding waybills')
