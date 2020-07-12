def row_name(self, self1, self2):  # 按照第一行对应的字段  读取整列数据
    # 5.历遍rows所有字段信息输出b1
    """
    :param self: 被查找的字段（“价格”、“货号”）
    :param self1: 被查找字段所在列
    :param self2: 被查找字段所在工作页
    :return:输出被查找字段对应一行的数据
    """

    x = 0
    for ii in self1:  # row是列
        # print('%s'%a,ii)

        aa = self  # 定位到【控制台】改列数据

        if aa == ii:  # 6.判断对应字段是第几列输出b1
            # print("输出：",'%s'%a)
            # print("%s"%aa,"存在第%s列"%a,rows[a])
            b1 = x
            # print("b1", b1)
            # print("输出：",'%s'%a)
            # print("cols:",cols)
            cols_b1 = self2.col_values(b1, 0)
            # print('定位好b1并读取',cols)
            # print("订单号", cols)
            # print(s)
        x = x + 1

    return cols_b1