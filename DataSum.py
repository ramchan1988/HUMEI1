"""
税金Tax.py统计主程序
"""

import pandas as pd
import RowData





def row_sum(rows, sheet):

    pp = []
    a1 = RowData.row_name("增值税", rows, sheet)
    a2 = RowData.row_name("消费税", rows, sheet)
    a3 = RowData.row_name("提运单号/转关单号", rows, sheet)
    a4 = RowData.row_name("海关状态", rows, sheet)
    ZZS = pd.Series(a1[2:], index=a3[2:], dtype=float)
    XFS = pd.Series(a2[2:], index=a3[2:], dtype=float)  # 第二单位
    HGZT = pd.Series(a4[2:], index=a3[2:])  # 第二单位
    HGZT = HGZT[HGZT == "放行"]
    x = set(a3[2:])
    _zzsSum = []
    _xfsSum = []
    #print("- - - - - - - - - - - - - - - - - - - -")
    for i in x:
        # print(i)
        if i not in [""]:

            # print(i)
            ZZS_0 = ZZS[i]
            pd.to_numeric(ZZS_0)
            ZZS_sum = ZZS_0.sum()
            _zzsSum.append(ZZS_sum)
            XFS_0 = XFS[i]
            pd.to_numeric(XFS_0)
            XFS_sum = XFS_0.sum()
            _xfsSum.append(XFS_sum)
            # print(HGZT[i])
            #print("提单号/转运单号", i, "增值税", ZZS_sum, "消费税", XFS_sum)

            p1="提单号/转运单号:"+ i+ " 增值税:"+str(ZZS_sum)+" 消费税:"+str(XFS_sum)
            #print("p1",p1)
            pp.append(p1)
            try:
                #print("放行数:", HGZT[i].count())
                p2="放行数:"+ str(HGZT[i].count())
                #print(p2)
            except:
                #print("放行数:", 1)
                p2="放行数:1"
                #print(p2)
            # print(ZZS_0.sum())
            pp.append(p2)
    #print("- - - - - - - - - - - - - - - - - - - -")

    #print("增值税合计：", pd.Series(_zzsSum).sum())
    p3="增值税合计："+ str(pd.Series(_zzsSum).sum())
    pp.append(p3)
    #print("消费税合计：", pd.Series(_xfsSum).sum())
    p4 ="消费税合计："+str(pd.Series(_xfsSum).sum())
    pp.append(p4)
    #print("总合计：", pd.Series(_xfsSum).sum() + pd.Series(_zzsSum).sum())
    p5="总合计："+str(pd.Series(_xfsSum).sum() + pd.Series(_zzsSum).sum())
    pp.append(p5)

    #print("- - - - - - - - - - - - - - - - - - - -")

    #print(pp)
    return pp
