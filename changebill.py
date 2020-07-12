"""
格式转换主程序
里面引用七个函数
"""


import os_file
import OpenExcel
import DataSum
import NewSheet
import RowData
import xlrd, xlwt
from xlutils.copy import copy as xl_copy
import datetime
import waybill
import re
import Delfile
import pandas as pd
import Formats
import logging



def heavy(cole_0, cole_1, cole_2, s):  # 【引用函数4】毛重净总按销量乘积
    print("├ 毛重净总按销量乘积----OK")
    jing_heavy = []
    for jz in range(len(cole_0) - 1):
        jing_heavy.append(cole_0[jz + 1] * cole_2[jz + 1])
        a = 1
        for x in jing_heavy:
            s.write(a, 30, x)
            a = a + 1
    mao_heavy = []
    for mz in range(len(cole_1) - 1):
        mao_heavy.append(cole_1[mz + 1] * cole_2[mz + 1])
        a = 1
        for x in mao_heavy:
            s.write(a, 31, x)
            a = a + 1
    # print(mao_heavy)
    # print(jing_heavy)


def firstrowname(cols, s):  # 【引用函数3】表头名字更正
    print("├ 项目名修正----OK")
    a = 0
    for x in cols:
        s.write(0, a, x)
        a = a + 1


def shu_liang(cols40, s):  # 【引用函数2】去掉0
    print("├ 0改成空----OK")
    # print(cols40)
    shuliang = []
    for i in range(1, len(cols40)):
        if cols40[i] == 0:
            a = ""
            shuliang.append(a)
        else:
            shuliang.append(cols40[i])
    a = 1
    for x in shuliang:
        s.write(a, 40, x)
        a = a + 1


def city_num(cols_0, s):  # 【引用函数1】省市代码转换函数
    print("├ 省市区代码调整----OK")
    sheet_0 = OpenExcel.open_excel_sheet("E:/HUMEI/Excel_shunxu/省市区/行政区域代码1.xlsx", sheet=0)
    row_1 = OpenExcel.open_excel_row("E:/HUMEI/Excel_shunxu/省市区/行政区域代码1.xlsx", sheet=0, row=0)
    cole_0 = RowData.row_name('区域', row_1, sheet_0)
    cole_1 = RowData.row_name('代码', row_1, sheet_0)
    # print(cole_0)
    # print(cole_1)
    citynum = {}  # 2个列表合并成一个字典
    a = 0
    for i in range(0, len(cole_0)):
        citynum[cole_0[a]] = cole_1[a]
        a = a + 1
    # print(citynum)
    daima = []
    a = 1
    for i in range(0, len(cols_0) - 1):
        dm = cols_0[a]
        # print("dm", dm)
        dm02 = citynum[dm]
        daima.append(dm02)
        a = a + 1
    # print(daima)
    a = 1
    for x in daima:
        s.write(a, 14, x)
        a = a + 1


def xun_hao(cols, s):  # 【引用函数0】序号重新排序函数
    print("├ 序号重新排列----OK")
    xuhao = []
    xuhao.append(1)
    a = 1
    for i in range(1, len(cols) - 1):
        if cols[i + 1] == cols[i]:  # 2比1
            xuhao.append(a + 1)
            a = a + 1
        else:
            a = 1
            xuhao.append(a)
    a = 1
    for x in xuhao:
        s.write(a, 22, x)
        a = a + 1


def mao_heavy_sum(cole_0, cole_1, cole_2, s):  # 【引用内部函数6】相同订单的毛重合计
    print("└ 相同订单的毛重合计----OK")
    mao_heavy = []
    for mz in range(len(cole_1) - 1):
        mao_heavy.append(cole_1[mz + 1] * cole_2[mz + 1])
    # ======================================================== #
    """
    相同订单号下面的毛重合计并且更改对应毛重
    """
    # ======================================================== #
    data = pd.DataFrame({'订单编号': cole_0[1:], '毛重': mao_heavy})
    dataA = data.groupby(by='订单编号').agg({'毛重': ["sum"]})
    # print(len(dataA))
    # print(dataA.index[0], dataA.values[0][0])
    heavysum = {}
    for mz in range(len(dataA)):
        # print(dataA.index[mz], dataA.values[mz][0])
        heavysum[dataA.index[mz]] = dataA.values[mz][0]
    # print(heavysum)
    # ======================================================== #
    mao_heavy_2 = []
    for orderid in cole_0[1:]:
        # print(orderid)
        # print(heavysum.get(orderid))
        mao_heavy_2.append(heavysum.get(orderid))
    # print("new", mao_heavy_2)
    a = 1
    for x in mao_heavy_2:
        s.write(a, 31, x)
        a = a + 1


def build_bill(ADD):
    # ADD = "E:/HUMEI/Excel_shunxu/检测/"
    ADD_none = r"E:\HUMEI\Excel_shunxu\空表\none.xls"
    ADD_changebill = "E:/HUMEI/Excel_shunxu/顺序模板/changebill_0.xls"

    all_file = os_file.open(self=ADD, all=1)
    # print("正在分析", all_file)
    row_changebill = OpenExcel.open_excel_row(ADD_changebill, sheet=0, row=0)
    # print(row_changebill)

    if len(all_file) > 0:  # 判断是否有文件

        p = 0
        for per_file in all_file:

            print("┌ 清单后期处理----Star")
            print("├", per_file)
            workbook_nome = xlrd.open_workbook(filename=ADD_none)
            wb = xl_copy(workbook_nome)
            try:
                s = wb.get_sheet(0)
            except:
                print("错误：请新建Sheet")
            sheet_0 = OpenExcel.open_excel_sheet(per_file, sheet=0)  # 读取第一个工作
            row_1 = OpenExcel.open_excel_row(per_file, sheet=0, row=0)  # 读取第一个工作页第一行
            # print(row_1)
            for i in range(45):
                a = 0
                for x in RowData.row_name(row_changebill[i], row_1, sheet_0):
                    s.write(a, i, x)
                    a = a + 1

            xun_hao(RowData.row_name("订单编号", row_1, sheet_0), s)  # 【引用内部函数0】序号重新排序函数
            city_num(RowData.row_name("收件人所在省*", row_1, sheet_0), s)  # 【引用内部函数1】省市代码转换函数
            shu_liang(RowData.row_name("第二法定数量*", row_1, sheet_0), s)  # 【引用内部函数2】去掉0
            firstrowname(OpenExcel.open_excel_row(ADD_changebill, sheet=0, row=1), s)  # 【引用内部函数3】表头名字更正
            heavy(RowData.row_name("净重", row_1, sheet_0),
                  RowData.row_name("毛重*", row_1, sheet_0),
                  RowData.row_name("申报数量*", row_1, sheet_0), s)  # 【引用内部函数4】毛重净总按销量乘积
            mao_heavy_sum(RowData.row_name("订单编号", row_1, sheet_0),
                          RowData.row_name("毛重*", row_1, sheet_0),
                          RowData.row_name("申报数量*", row_1, sheet_0), s)  # 【引用内部函数6】相同订单的毛重合计

            new_name = re.findall("/检测/(.+).xls", per_file)
            # print(new_name)
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d_%H：%M：%S')
            # print(type(nowTime))
            # print(RowData.row_name("序号", row_1, sheet_0))
            # wb.save("E:/HUMEI/Excel_shunxu/检测1/"+"changebill_%s.xls" % nowTime)
            p = p + 1
            wb.save("E:/HUMEI/Excel_shunxu/检测1/" + "%s_%s %s.xls" % (new_name[0], nowTime, p))
            wb.save("E:/HUMEI/Excel_shunxu/检测3/" + "%s_%s %s.xls" % (new_name[0], nowTime, p))
            wb.save("E:/HUMEI/Excel_shunxu/转发1/" + "%s_%s %s.xls" % (new_name[0], nowTime, p))
        print("清单生成----OK")
    else:
        logging.info("生成%s份清单文件" % len(all_file))
        #print()
        return "生成%s份清单文件" % len(all_file)


def run():
    try:

        #print('**开始**')
        ADD = "E:/HUMEI/Excel_shunxu/检测/"
        Formats.formast(ADD)  # 格式转换
        build_bill(ADD)  # 清单生成
        waybill.build_waybill()  # 运单生成
        #print("运单生成----OK")
        Delfile.delfile("E:/HUMEI/Excel_shunxu/检测1/")  # 【引用外部函数5】清空文件夹内文件
        #print('**结束**')
        logging.info("处理完成")
        # input()
        return "success"
    except:
        logging.info("格式错误,请联系管理员")
        return "格式错误,请联系管理员"


if __name__ == '__main__':
    run()
