import xlrd


def open_excel_sheet(self, sheet=0):  # 批量读取list的文件
    """
    :param self: excel文件的路径
    :param sheet: excel文件对应第几个工作页
    :return: 输出对应工作页的内存编号
    """
    workbook = xlrd.open_workbook(filename=self)  # 用【xlrd库】读取*.xls文件
    sheet1 = workbook.sheet_by_index(sheet)  # 读取第一个工作页
    return sheet1  # 输出工作页


def open_excel_row(self, sheet=0, row=0):  # 批量读取list的文件
    """
    :param self: excel文件的路径
    :param sheet: excel文件对应第几个工作页
    :param row: excel文件对应的第几列数据
    :return: 输出指定列的数据
    """
    workbook = xlrd.open_workbook(filename=self)  # 【xlrd库】读取*.xls文件
    sheet1 = workbook.sheet_by_index(sheet)  # 读取第一个工作页
    rows = sheet1.row_values(row)  # 读取第一页的第一行
    return rows  # 输出行
