# -*- coding: utf-8 -*-

'''
哈希256签名 ； RSA加密解密  第三版本
'''

import hashlib as hasher
import logging
import rsa
import datetime as date
import numpy as np
import pandas as pd
# ------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),

# ------------------------------

def hash_block(data):  # 哈希转换
    sha = hasher.sha256()
    data=data
    sha.update(data)
    #logging.info(sha.hexdigest())
    return sha.hexdigest()


# rsa加密
def rsaEncrypt(self):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    print("身份码:\n%s\n密匙:\n:%s" % (pubkey, privkey))  # 身份码pubkey=公匙  密匙=秘钥privkey
    # 明文编码格式
    content = self.encode("utf-8")
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(self, privkey):
    # 私钥解密
    content = rsa.decrypt(self, privkey)
    con = content.decode("utf-8")
    return con


class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash # 身份证的哈希
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        hash_data = bytes(
                str(self.index) + str(self.timestamp) + str(self.data) + str(
                    self.previous_hash), 'utf-8')
        sha.update(hash_data)

        return sha.hexdigest()




def create_genesis_block(name): # 创建区块
    #block=Block(0, date.datetime.now(), "Genesis Block", "0")
    #  Manually construct a block with index 0 and arbitrary previous hash
    name=str(name)
    return Block(0, date.datetime.now(), "Genesis Block",name)


def next_block(last_block,data,last_block_hash,name): # 生成区块
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data ="区块号:"+ str(this_index) +",记录员ID:"+str(name)+",内容:"+str(data) +",记录时间:"+ str(this_timestamp)+",上一个区块哈希值:"+str(last_block_hash)
    """
    this_data：记录区块内容
    """
    name = name  # 输入者的身份号的哈希
    return Block(this_index, this_timestamp, this_data, name)


def first_run(name):  # 创建第一个区块
    """
    用字典记录每一个区块 index=区块编号
    :param name: 录入人id
    :return:
    """
    b={}
    b["0"]=create_genesis_block(name)
    np.save('bolck_link_2.npy', b)
    find_name={}


    hdata = bytes(str(b[str(0)].index) +","+ str(b[str(0)].timestamp)+"," + str(b[str(0)].data) +","+ str(b[str(0)].previous_hash),
                  'utf-8')
    """
    hdata:组合成区块链的内容
    """
    find_name[str(hdata.decode())]=str(name)  # key=姓名 值=内容 保存字典
    print(find_name)
    np.save('bolck_link_name_2.npy', find_name)
    print(b["0"].index,b["0"].data,b["0"].timestamp,b["0"].hash)



def run(self,name):  # 新增区块
    """

    :param self: 记录的主要内容
    :param name: 记录人
    :return:
    """
    try:
        # ------------------------ 表1以区块编号保存dict ------------------
        # data=input().__str__()
        b = np.load('E:/HUMEI/bolck_link_2.npy', allow_pickle=True).item()

        logging.info(b)
        print(len(b.keys()), type(len(b.keys())))
        data = str(self)   # 输入内容
        i = len(b.keys()) - 1
        # print(i, type(i))
        i_new = len(b.keys())
        """
        i,i_new:区块编号
        """
        print("101行", b[str(i)].index, data, b[str(i)].hash_block())
        block_to_add = next_block(b[str(i)], data, b[str(i)].hash_block(),str(name))
        logging.info(block_to_add)
        logging.info("成功")
        b[str(i_new)] = block_to_add  # 序号记录保存区块信息
        np.save('E:/HUMEI/bolck_link_2.npy', b)   # 先保存到总表

        # ------------------------ 表2以名字保存dict ------------------
        b = np.load('E:/HUMEI/bolck_link_2.npy', allow_pickle=True).item()
        find_name = np.load('E:/HUMEI/bolck_link_name_2.npy', allow_pickle=True).item()
        print("123",find_name)
        '''
        hdata = bytes(
            str(b[str(i)].index) + str(b[str(i)].timestamp) + str(b[str(i)].data) + str(b[str(i)].previous_hash),
            'utf-8')
        '''
        ii=len(b.keys())-1
        hdata = bytes(str(b[str(ii)].index) + "," + str(b[str(ii)].timestamp) + "," + str(b[str(ii)].data) + "," + str(
            b[str(ii)].previous_hash),
                      'utf-8')
        print("132",hdata)
        find_name[str(hdata.decode())] = str(name)
        print(find_name)

        np.save('E:/HUMEI/bolck_link_name_2.npy', find_name)




        # return "处理成功%s%s%s%s"%(b[str(i)].index, data, b[str(i)].hash_block())
        return "区块编码:" + str(b[str(i)].index+1) +"<br>"+"区块信息:<br>" + str(data)+"<br>" +"哈希值:" + str(b[str(i)].hash_block())

    except:
        return print("上链失败")


def run_find(self):
    b = np.load('E:/HUMEI/bolck_link_2.npy', allow_pickle=True).item()
    k= str(self)
    # hdata = bytes(str(b[str(k)].index) +str(b[str(k)].timestamp)  + str(b[str(k)].data) + str(b[str(k)].previous_hash), 'utf-8')
    hdata = bytes(str(b[str(k)].index) + str(b[str(k)].timestamp) +  str(b[str(k)].data) +  str(
        b[str(k)].previous_hash),
                  'utf-8')
    print("第三方查验码：")
    print(str(hdata.decode()))

    # hdata=bytes("123",'utf-8')
    hdata = str(hdata.decode()).encode("utf-8")
    print("输出这个:",hdata)
    print("SHA256验证结果(比对第三方验证结果)")
    print(hash_block(hdata))
    return  "区块存储信息:<br>"+b[str(k)].data+"<br>"+"当前区块哈希值:<br>"+b[str(k)].hash_block()+"<br>"+"查验码(sha256加密后与本区块哈希值比较):<br>"+str(hdata.decode())


def run_find_name(nameid):
    find_name = np.load('E:/HUMEI/bolck_link_name_2.npy', allow_pickle=True).item()
    #print(find_name)
    d = pd.Series(list(find_name.keys()), list(find_name.values()))
    d.index.name = "ID"
    d.name = "data"
    #print(type(str(nameid)))
    print(d[nameid])
    #d=d[str(nameid)].astype(str)

    #print(d)
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
        return nameid+":"+d

    





if __name__ == '__main__':
    s, privkey = rsaEncrypt("234234sdfsdf")
    print("加密后密文：\n%s" % s)
    content = rsaDecrypt(s, privkey)
    print("解密后明文：\n%s" % content)








    #first_run()
    #hash_block("good")
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


