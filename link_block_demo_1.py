# -*- coding: utf-8 -*-

'''
哈希256签名 ； RSA加密解密
'''

import hashlib as hasher
import logging
import rsa
import datetime as date
import numpy as np

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
        self.previous_hash = previous_hash # 身份证的哈希
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        hash_data = bytes(
                str(self.index) + str(self.timestamp) + str(self.data) + str(
                    self.previous_hash), 'utf-8')
        sha.update(hash_data)

        return sha.hexdigest()




def create_genesis_block(): # 创建区块
    #block=Block(0, date.datetime.now(), "Genesis Block", "0")
    #  Manually construct a block with index 0 and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0",)


def next_block(last_block,data,last_block_hash): # 生成区块
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "记录的内容:"+str(data) +" 区块编号:"+ str(this_index) +" 记录时间:"+ str(this_timestamp)+" 上一个区块哈希值"+str(last_block_hash)
    this_hash = "1d31"  # 输入者的身份号哈希
    return Block(this_index, this_timestamp, this_data, this_hash)


def first_run():
    b={}
    b["0"]=create_genesis_block()
    np.save('bolck_link.npy', b)
    print(b["0"].index,b["0"].data,b["0"].timestamp,b["0"].hash)



def run(self):
    try:
        # data=input().__str__()
        b = np.load('E:/HUMEI/bolck_link.npy', allow_pickle=True).item()
        logging.info(b)
        # name = input('请输入您的用户名：')
        print(len(b.keys()), type(len(b.keys())))
        data = str(self)
        i = len(b.keys()) - 1
        # print(i, type(i))
        i_new = len(b.keys())
        print("101行", b[str(i)].index, data, b[str(i)].hash_block())
        block_to_add = next_block(b[str(i)], data, b[str(i)].hash_block())
        logging.info(block_to_add)
        logging.info("成功")
        b[str(i_new)] = block_to_add
        np.save('E:/HUMEI/bolck_link.npy', b)

        # return "处理成功%s%s%s%s"%(b[str(i)].index, data, b[str(i)].hash_block())
        return "区块编码:" + str(b[str(i)].index+1) +"<br>"+"区块信息:<br>" + str(data)+"<br>" +"哈希值:" + str(b[str(i)].hash_block())

    except:
        return "上链失败"


def run_find(self):
    b = np.load('E:/HUMEI/bolck_link.npy', allow_pickle=True).item()
    k= str(self)
    hdata = bytes(str(b[str(k)].index) +str(b[str(k)].timestamp)  + str(b[str(k)].data) + str(b[str(k)].previous_hash), 'utf-8')
    print("第三方查验码：")
    print(str(hdata.decode()))
    # hdata=bytes("123",'utf-8')
    #hdata = str(hdata.decode()).encode("utf-8")
    #print(hdata)
    #print("SHA256验证结果(比对第三方验证结果)")
    #print(hash_block(hdata))
    return  b[str(k)].data+"<br>"+"当前区块哈希值"+b[str(k)].hash_block()+"<br>"+"第三方查验码:"+str(hdata.decode())







if __name__ == '__main__':
    print(run_find(3))




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


