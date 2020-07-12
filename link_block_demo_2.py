# -*- coding: utf-8 -*-

'''
哈希256签名 ； RSA加密解密
'''

import hashlib as hasher
import logging
import rsa
import datetime as date
import numpy as np
import pandas as pd
import re

# ------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),


# ------------------------------

def hash_block(data):  # 哈希转换
    sha = hasher.sha256()
    data = data
    sha.update(data)
    # logging.info(sha.hexdigest())
    return sha.hexdigest()


# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    print("身份码:\n%s\n密匙:\n:%s" % (pubkey, privkey))  # 身份码=公匙  密匙=秘钥
    # 明文编码格式
    content = str.encode("utf-8")
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode("utf-8")
    return con


class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash  # 身份证的哈希
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        hash_data = bytes(
            str(self.index) + str(self.timestamp) + str(self.data) + str(
                self.previous_hash), 'utf-8')
        sha.update(hash_data)

        return sha.hexdigest()


def create_genesis_block(name):  # 创建区块
    # block=Block(0, date.datetime.now(), "Genesis Block", "0")
    #  Manually construct a block with index 0 and arbitrary previous hash
    name = str(name)
    return Block(0, date.datetime.now(), "Genesis Block", name)


def next_block(last_block, data, last_block_hash, name):  # 生成区块
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "区块号:" + str(this_index) + ",记录员ID:" + str(name) + ",内容:" + str(data) + ",记录时间:" + str(
        this_timestamp) + ",上一个区块哈希值:" + str(last_block_hash)
    name = name  # 输入者的身份号哈希
    return Block(this_index, this_timestamp, this_data, name)


def first_run(name):
    b = {}
    b["0"] = create_genesis_block(name)
    np.save('bolck_link_2.npy', b)
    find_name = {}

    hdata = bytes(str(b[str(0)].index) + "," + str(b[str(0)].timestamp) + "," + str(b[str(0)].data) + "," + str(
        b[str(0)].previous_hash),
                  'utf-8')

    # print("第三方查验码：")
    # print(str(hdata.decode()))
    find_name[str(hdata.decode())] = str(name)
    print(find_name)
    np.save('bolck_link_name_2.npy', find_name)
    print(b["0"].index, b["0"].data, b["0"].timestamp, b["0"].hash)


def run(self, name):
    if name == "" or self == "":
        print("不能输入空值")
        return "不能输入空值"

    else:
        try:
            # data=input().__str__()
            b = np.load('E:/HUMEI/bolck_link_2.npy', allow_pickle=True).item()

            logging.info(b)
            # name = input('请输入您的用户名：')
            print(len(b.keys()), type(len(b.keys())))
            data = str(self)
            i = len(b.keys()) - 1
            # print(i, type(i))
            i_new = len(b.keys())
            print("101行", b[str(i)].index, data, b[str(i)].hash_block())
            block_to_add = next_block(b[str(i)], data, b[str(i)].hash_block(), str(name))
            logging.info(block_to_add)
            logging.info("成功")
            b[str(i_new)] = block_to_add
            np.save('E:/HUMEI/bolck_link_2.npy', b)

            # ------------------------ 以名字保存dict ------------------
            b = np.load('E:/HUMEI/bolck_link_2.npy', allow_pickle=True).item()
            find_name = np.load('E:/HUMEI/bolck_link_name_2.npy', allow_pickle=True).item()
            print("123", find_name)
            '''
            hdata = bytes(
                str(b[str(i)].index) + str(b[str(i)].timestamp) + str(b[str(i)].data) + str(b[str(i)].previous_hash),
                'utf-8')
            '''
            ii = len(b.keys()) - 1
            hdata = bytes(
                str(b[str(ii)].index) + "," + str(b[str(ii)].timestamp) + "," + str(b[str(ii)].data) + "," + str(
                    b[str(ii)].previous_hash),
                'utf-8')
            print("132", hdata)
            find_name[str(hdata.decode())] = str(name)
            print(find_name)

            np.save('E:/HUMEI/bolck_link_name_2.npy', find_name)

            # return "处理成功%s%s%s%s"%(b[str(i)].index, data, b[str(i)].hash_block())
            return "区块编码:" + str(b[str(i)].index + 1) + "<br>" + "区块信息:<br>" + str(data) + "<br>" + "哈希值:" + str(
                b[str(i)].hash_block())
        except:
            print("上链失败")
            return "上链失败"


def run_find(self):
    b = np.load('E:/HUMEI/bolck_link_2.npy', allow_pickle=True).item()
    k = str(self)
    # hdata = bytes(str(b[str(k)].index) +str(b[str(k)].timestamp)  + str(b[str(k)].data) + str(b[str(k)].previous_hash), 'utf-8')
    hdata = bytes(str(b[str(k)].index) + str(b[str(k)].timestamp) + str(b[str(k)].data) + str(
        b[str(k)].previous_hash),
                  'utf-8')
    print("第三方查验码：")
    print(str(hdata.decode()))

    # hdata=bytes("123",'utf-8')
    hdata = str(hdata.decode()).encode("utf-8")
    print("输出这个:", hdata)
    print("SHA256验证结果(比对第三方验证结果)")

    print(hash_block(hdata))
    return "Data:<br>" + b[str(k)].data + "<br><br>" + "Hash:<br>" + b[
        str(k)].hash_block() + "<br><br>" + "查验码(sha256加密后与本区块哈希值比较):<br>" + str(hdata.decode())


def run_find_name(nameid):
    find_name = np.load('E:/HUMEI/bolck_link_name_2.npy', allow_pickle=True).item()
    # print(find_name)
    d = pd.Series(list(find_name.keys()), list(find_name.values()))
    d.index.name = "ID"
    d.name = "data"
    # print(type(str(nameid)))
    print(d[nameid])
    # d=d[str(nameid)].astype(str)

    # print(d)
    d = d[str(nameid)]
    try:

        d.to_csv("data_test_name_2.csv")

        data = pd.read_csv("data_test_name_2.csv")
        sl = data.values.tolist()

        # sl=str(sl)
        name_id = [str(sl[i][0]) + ": " + str(sl[i][1]) for i in range(len(sl))]

        s = ''
        for i in name_id:
            s = s + i + "<br>"

        return s
    except:
        return nameid + ":" + d


def run_find_name_test_demo(nameid):
    find_name = np.load('E:/HUMEI/bolck_link_name_2.npy', allow_pickle=True).item()

    d = pd.Series(list(find_name.keys()), list(find_name.values()))
    d.index.name = "ID"
    d.name = "data"
    # print(type(str(nameid)))
    print(d)
    print(d[nameid])
    # d=d[str(nameid)].astype(str)

    # print(d)
    d = d[str(nameid)]
    try:

        d.to_csv("data_test_name_2.csv")

        data = pd.read_csv("data_test_name_2.csv")
        sl = data.values.tolist()

        # sl=str(sl)
        _name_id = [str(sl[i][0]) + ": " + str(sl[i][1]) for i in range(len(sl))]
        name_id = [str(sl[i][0]) for i in range(len(sl))]
        # print(name_id)
        name_data = [str(sl[i][1]) for i in range(len(sl))]
        # print(name_data)
        # print(len(name_id))

        s = ''
        A = "<td><a href='/linkfind=%s' role='button' data-toggle='modal' ><i class='fa fa-pencil'></i></a></td>"
        # B="<div class='modal small fade' id='myModal' tabindex='-1' role='dialog' aria-labelledby='myModalLabel' aria-hidden='true' style='display: none;'><div class='modal-dialog'><div class='modal-content'><div class='modal-header'><button type='button' class='close' data-dismiss='modal' aria-hidden='true'>×</button><h3 id='myModalLabel'>详情</h3></div><div class='modal-body'><p class='error-text'><i class='fa fa-warning modal-icon'></i>查看区块详细信息</p></div><div class='modal-footer'><button class='btn btn-default' data-dismiss='modal' aria-hidden='true'>取消</button><button class='btn btn-danger' data-dismiss='modal' onclick=jump_xx()>确认</button></div></div></div></div>"
        for i in range(len(name_id)):
            dd = re.compile(r'内容:(.+?),记录时间')
            link_data = dd.findall(name_data[i])
            link_data.append(" ")

            dd = re.compile(r'(.+?),202')
            link_number = dd.findall(name_data[i])

            dd = re.compile(r',(.+?),区块号')
            link_time = dd.findall(name_data[i])
            link_time.append(" ")
            print(link_time)

            s = s + "<tr><td>" + str(i + 1) + "</td><td>" + name_id[i] + "</td><td>" + link_number[0] + "</td><td>" + \
                link_time[0] + "</td><td>" + link_data[0] + "</td>" + A % link_number[0] + "</tr>"
            # print(i,s)

        s = s
        return s
    except:
        print("123", type(d))

        dd = re.compile(r'内容:(.+?),记录时间')
        link_data = dd.findall(str(d))
        link_data.append(" ")
        print(link_data)

        dd = re.compile(r'(.+?),202')
        link_number = dd.findall(str(d))
        print(link_number)
        dd = re.compile(r',(.+?),区块号')
        link_time = dd.findall(str(d))
        link_time.append(" ")
        print(link_time)
        A = "<td><a href='/linkfind=%s' role='button' data-toggle='modal' ><i class='fa fa-pencil'></i></a></td>"
        # return nameid+":"+d
        print("<tr><td>" + "1" + "</td><td>" + str(nameid) + "</td><td>" + link_number[0] + "</td><td>" + link_time[
            0] + "</td><td>" + link_data[0] + "</td>" + A % link_number[0] + "</tr>")
        return "<tr><td>" + "1" + "</td><td>" + str(nameid) + "</td><td>" + link_number[0] + "</td><td>" + link_time[
            0] + "</td><td>" + link_data[0] + "</td>" + A % link_number[0] + "</tr>"


#  =========          run_find_name_test_demo        ==================
def npy_to_df_v1(file):
    b = np.load(file, allow_pickle=True).item()
    # print(b)
    link_id = [b[i].index for i in b.keys()]
    print(link_id)
    link_time = [b[i].timestamp.strftime('%Y-%m-%d %H:%M:%S') for i in b.keys()]
    print(link_time)
    link_data = [b[i].data for i in b.keys()]
    print(link_data)
    link_hash = [b[i].previous_hash for i in b.keys()]
    print(link_hash)
    df = pd.DataFrame({"linkid": link_id, "time": link_time, "data": link_data, "name": link_hash})
    return df


def search_date_v1(df, time1, time2):
    print(df)
    print("==================")
    print(df.dtypes)
    df['time'] = pd.to_datetime(df['time'])  # 将数据类型转换为日期类型
    df = df.set_index('time')  # 将date设置为index
    print("==================")
    print(df)
    print("=======指定日期===========")
    df = df[time1:time2]
    print(df)
    return df


def x_run(df, i, s):
    # print("=======指定列===========")
    # print(df["data"][i])
    link_id_per = re.compile(s)
    link_id_per = link_id_per.findall(df["data"][i])
    # print(link_id_per)
    return link_id_per


def run_find_time_test_demo():
    file = 'E:/HUMEI/bolck_link_2.npy'
    df = npy_to_df_v1(file)
    time1 = "2020-06-24"
    time2 = "2020-06-26"
    df = search_date_v1(df, time1, time2)
    print(len(df))
    link_data_a = [x_run(df, i, r'内容:(.+?),') for i in range(len(df))]
    print("内容", link_data_a)
    name_id_a = [x_run(df, i, r'记录员ID:(.+?),') for i in range(len(df))]
    print("记录员", name_id_a)
    Hash_a = [x_run(df, i, r'上一个区块哈希值:(.+)') for i in range(len(df))]
    print("哈希值", Hash_a)
    link_time_a = [x_run(df, i, r'记录时间:(.+),') for i in range(len(df))]
    print("时间戳", link_time_a)
    link_number_a=[x_run(df,i,r'区块号:(.+?),') for i in range(len(df))]
    print("区块编号",link_number_a)


    s = ''
    A = "<a href='/linkfind=%s' role='button' data-toggle='modal' ><i class='fa fa-pencil'></i></a>"
    # B="<div class='modal small fade' id='myModal' tabindex='-1' role='dialog' aria-labelledby='myModalLabel' aria-hidden='true' style='display: none;'><div class='modal-dialog'><div class='modal-content'><div class='modal-header'><button type='button' class='close' data-dismiss='modal' aria-hidden='true'>×</button><h3 id='myModalLabel'>详情</h3></div><div class='modal-body'><p class='error-text'><i class='fa fa-warning modal-icon'></i>查看区块详细信息</p></div><div class='modal-footer'><button class='btn btn-default' data-dismiss='modal' aria-hidden='true'>取消</button><button class='btn btn-danger' data-dismiss='modal' onclick=jump_xx()>确认</button></div></div></div></div>"


    for i in range(len(link_data_a)):

        if len(name_id_a[i])>0:
            #print("非0")
            s = s + \
                "<tr>" + \
                "<td>" + str(i + 1) + "</td>" + \
                "<td>" + name_id_a[i][0] + "</td>" + \
                "<td>" + link_number_a[i][0] + "</td>" + \
                "<td>" + link_time_a[i][0][0:19] + "</td>" + \
                "<td>" + link_data_a[i][0] + "</td>" + \
                "<td>" + A % link_number_a[i][0] + "</td>" + \
                "</tr>"
            #print(i, s)
        else:
            #print("0号")
            s = s + \
                "<tr>" + \
                "<td>" + "1" + "</td>" + \
                "<td>" + "ramchan1988" + "</td>" + \
                "<td>" + "0" + "</td>" + \
                "<td>" + "2020-06-24 17:58:13" + "</td>" + \
                "<td>" + "Genesis Block" + "</td>" + \
                "<td>" + A % "0" + "</td>" + \
                "</tr>"




    s = s
    #print(s)
    return s




"""
        try:    
        except:
            s = s + \
                "<tr>" + \
                "<td>" + "1" + "</td>" + \
                "<td>" + "Genesis Block" + "</td>" + \
                "<td>" + "0" + "</td>" + \
                "<td>" + "2020-06-24 17:58:13" + "</td>" + \
                "<td>" + "Genesis Block" + "</td>" + \
                "<td>" + A % "0" + "</td>" + \
                "</tr>"
            print(i, s)
"""










#  =========          run_find_name_test_demo        ==================





if __name__ == '__main__':
    # first_run("ramchan1988")
    # run("物流号23521245631", "rr")

    # print("199",type(run_find_name("124587")))
    #print("s", run_find_name_test_demo("ram1988"))
    run_find_time_test_demo()

    # first_run()
    # hash_block("good")
'''
    print("创建账号")
    str1=input("输入密码：").__str__()
    print("创建成功，请不要泄露密码和密匙")
    str1,pk=rsaEncrypt(str1)
    content = rsaDecrypt(str1, pk)
    #print("解密后明文：\n%s" % content,type(content))

    print("创建区块")
    while True:
        b = np.load('bolck_link.npy', allow_pickle=True).item()
        #name = input('请输入您的用户名：')
        print(len(b.keys()),type(len(b.keys())))
        data = input()
        i=len(b.keys())-1
        print(i,type(i))
        i_new=len(b.keys())
        print(b[str(i)].index, data, b[str(i)].hash_block())
        block_to_add = next_block(b[str(i)], data, b[str(i)].hash_block())
        b[str(i_new)]=block_to_add
        np.save('bolck_link.npy', b)

'''

'''
    for i in range(0, 20):
        data=input()
        block_to_add = next_block(previous_block,data,blockchain[i].hash_block())

        blockchain.append(block_to_add)
        previous_block = block_to_add
        #  Tell everyone about it!
        print("Block #{} has been added to the"
              "blockchain!".format(block_to_add.index))
        print(blockchain[i+1].data)
        print("当前区块哈希值: {}\n".format(block_to_add.hash))
        print("录入信息者身份码:",blockchain[i+1].previous_hash)
        hdata=bytes(str(blockchain[i+1].index) + str(blockchain[i+1].timestamp) + str(blockchain[i+1].data) + str(
                    blockchain[i+1].previous_hash),'utf-8')
        print("本区块查验信息:")
        print(str(hdata.decode()))
        #hdata=bytes("123",'utf-8')
        hdata=str(hdata.decode()).encode("utf-8")
        print("SHA256验证结果(比对第三方验证结果)")
        print(hash_block(hdata))
'''
