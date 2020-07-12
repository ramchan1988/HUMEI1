import os_file
import OpenExcel
import DataSum
import ListToStr
import logging
import os
# ------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),

# ------------------------------

ADD = "E:/HUMEI/Excel_shunxu/税金/"

def tax_main_(ADD):
    s=""
    all_file = os_file.open(self=ADD, all=1)
    # print(len(all_file))
    if len(all_file) > 0:
        for per_file in all_file:
            print("读取", per_file)
            # print(per_file)
            sheet_0 = OpenExcel.open_excel_sheet(per_file, sheet=0)
            try:
                row_1 = OpenExcel.open_excel_row(per_file, sheet=0, row=1)  # row=1 第二行
                tostr = ListToStr.tostr(DataSum.row_sum(rows=row_1, sheet=sheet_0))  # 转成文本
            # print("sheet",sheet_0)
            # print("row", row_1)
            #print(type(DataSum.row_sum(rows=row_1, sheet=sheet_0)))
            except:
                #os.remove(per_file)
                tostr = "格式不对<br>"
            #logging.info(tostr)
            #return tostr
            s=s+per_file+"<br>"+tostr+"<br>"
            #logging.info(s)
            # return DataSum.row_sum(rows=row_1, sheet=sheet_0)
    else:
        return "找不到文件"
        print("已计算%s份文件的税金" % len(all_file))
    return s


if __name__ == '__main__':
    print('**开始**')
    print(tax_main_(ADD))
    print('**结束**')
