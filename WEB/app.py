# -*- coding: utf-8 -*-

'''
多功能操作页面
'''

from flask import Flask, render_template
import logging
import Tax
import movefile
import changebill
import send_email_ok
import time_call_one
import Delfile
from concurrent.futures import ThreadPoolExecutor
import find_file_h5
import PaChong_qw
import link_block_demo_1
import link_block_demo_2
import hashlib as hasher
import time
import asyncio
import datetime as date
# ------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="\033[34m[%(asctime)s] [%(filename)s] (%(levelname)s-第%(lineno)d行)\n%(message)s\033[0m"),

# ------------------------------

app = Flask(__name__)

'''
@app.route('/11123')
def hello_world():
    #return "ddd"
    try:
        old_str = "这里是最新的内容……"  # 老文件内容字段
        new_str = "aaa"  # 要改成字段
        file_data = ''
        with open(file='file/good.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                if old_str in line:
                    line = line.replace(old_str, new_str)
                file_data += line
                # logging.info(file_data)
        f.close()
        with open(file='static/js/button_0.js', mode='w', encoding='utf-8') as f:
            f.write(file_data)
        f.close()

        logging.info(f)
        return render_template('hello world.html')
    except:
        return "no"
'''




def insertStr(new_str):  # 插入字符串
    # 有一个字符串
    old_str = "*"
    # new_str="112"
    file_data = ""
    with open(file='file/nice2_tax', mode='r', encoding='utf-8') as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    f.close()
    # 把字符串转为 list
    logging.info(file_data)
    return file_data
    # 字符数， 可以利用这个在某个位置插入字符
    # count = len(str_list)
    # 找到 斜杠的位置


'''
    nPos = str_list.index('*')
    # 在斜杠位置之前 插入要插入的字符
    str_list.insert(nPos, '佳人何处在!')
    # 将 list 转为 str
    str_2 = "".join(str_list)
    print(str_2)
'''


@app.route('/b', endpoint="b")  # 税金查询
# @time_call_one.stat_called_time
def hello_world_2():
    ADD = "E:/HUMEI/Excel_shunxu/税金/"
    hello()
    data = hello()
    logging.info(data)
    # data = insertStr(data)
    # logging.info(data)
    # return data
    return render_template("index.html", name=data, name_2="查税金")
    # return render_template('test1.html')


@app.route('/')  # 首页
def hello_world_a():
    return render_template('index.html', name_2="欢迎登陆")


# ============================================区块链=============================================



@app.route('/link')  # 区块链
def link_1():
    return render_template('link2.html', name_2="创建区块链",name_3="反馈内容")



@app.route('/linkup=<link>', endpoint="linkup_1")  # 这个暂时没有用
#@time_call_one.stat_called_time
def link_1(link):
    logging.info("ok")
    linkdata=link
    logging.info(link)
    a = link_block_demo_1.run(linkdata)
    return render_template('link2.html', name="信息不能为空", name_2="信息录入", name_3="处理结果")


@app.route('/linkup=<link>=<linkname>', endpoint="linkup_2")  # 记录新区块 第二版本
#@time_call_one.stat_called_time
def link_1(link,linkname):
    logging.info("ok")
    linkdata=link
    a = link_block_demo_2.run(linkdata,linkname)
    return render_template('link2.html', name=a, name_2="信息录入" ,name_3="处理结果")


@app.route('/linkfindname', endpoint="linkup_name")  # 以区块编号搜索
#@time_call_one.stat_called_time
def run_find_name():
    return render_template('link3nameDemo.html',name_3="处理结果")



@app.route('/linkfindname=<linknameID>', endpoint="linkup_name_1")  # 搜索
#@time_call_one.stat_called_time
def run_find_name_1(linknameID):
    logging.info("ok")
    try:
        _a = link_block_demo_2.run_find_name(linknameID)
        a = link_block_demo_2.run_find_name_test_demo(linknameID)
        print(a)
        #return render_template('link3name.html', name=a, name_3="处理结果")
        return render_template('link3nameDemo.html', name=a, name_3="处理结果")
    except:
        return render_template('link2.html', name="找不到用户信息", name_3="处理结果")




@app.route('/linkfind=<linkfind>', endpoint="linkfind_1")  # 搜索
#@time_call_one.stat_called_time
def link_find(linkfind):
    if linkfind == "":
        return render_template('link2.html', name="找不到区块", name_3="查找结果")
    else:
        try:
            a = link_block_demo_2.run_find(linkfind)
            return render_template('link2.html', name=a, name_3="查找结果",name_2="区块查找")
        except:
            return render_template('link2.html', name="找不到区块", name_3="查找结果",name_2="区块查找")


@app.route('/linkfind=', endpoint="linkfind_2")  # 搜索
#@time_call_one.stat_called_time
def link_find_no():
    return render_template('link2.html', name="找不到区块", name_3="查找结果")



@app.route('/linktime', endpoint="linkfind_time_1")  # 搜索
#@time_call_one.stat_called_time
def link_find_time():
    try:
        a = link_block_demo_2.run_find_time_test_demo()
        print(a)
        # return render_template('link3name.html', name=a, name_3="处理结果")
        return render_template('link3time.html', name=a, name_3="处理结果")
    except:
        return render_template('link2.html', name="找不到结果", name_3="处理结果")











# ============================================区块链=============================================




@app.route('/help')  # 帮助
def help_1():
    return render_template('index.html', name_2="帮助")


@app.route('/a')  # 一键转换 转换格式发送邮件
@time_call_one.stat_called_time
def web_changebill():
    ADD = "E:/HUMEI/Excel_shunxu/检测/"
    src_path = 'D:/新建文件夹/WeChat Files/wxid_6xnvlbwhpof321/FileStorage/File/2020-07/'
    txt = "我要转换"
    sendemadladd = "E:/HUMEI/Excel_shunxu/转发1/"
    Delfile.delfile(sendemadladd)  # 清空文件夹
    Delfile.delfile(ADD)
    movefile.run(src_path, ADD, txt)  # 文件移动到ADD
    try:
        changebill.run()
    except Exception as e:
        print(e)
        return render_template("index.html", name="转换失败", name_2="转换格式")
        # return "转换失败" + "<ul><li><a href='/'>返回</a></li></ul>"
    try:
        print("发邮件")
        #send_email_ok.run(sendemadladd)  # 发邮件
    except Exception as e:
        print(e)
        # return "处理失败" + "<ul><li><a href='/'>返回</a></li></ul>"
        return render_template("index.html", name="处理失败", name_2="转换格式")
    time.sleep(1)
    Delfile.delfile(sendemadladd)  # 清空
    Delfile.delfile(ADD)   # 清空
    # return "处理成功" + "<ul><li><a href='/'>返回</a></li></ul>"
    return render_template("index.html", name="处理成功", name_2="转换格式")


def hello() -> str:  # 转移文件并执行函数
    ADD = "E:/HUMEI/Excel_shunxu/税金/"
    src_path = 'D:/新建文件夹/WeChat Files/wxid_6xnvlbwhpof321/FileStorage/File/2020-06/'
    txt = "我要查税金"
    movefile.run(src_path, ADD, txt)
    print(Tax.tax_main_(ADD))
    return Tax.tax_main_(ADD)


@app.route('/c', endpoint="c")  # 清空文件夹
@time_call_one.stat_called_time
def web_delfile():
    try:
        ADD = "E:/HUMEI/Excel_shunxu/税金/"
        Delfile.delfile(ADD)
        # return "处理成功" + "<ul><li><a href='/'>返回</a></li></ul>"
        return render_template("index.html", name="处理成功", name_2="清空数据")
    except:
        # return "处理失败" + "<ul><li><a href='/'>返回</a></li></ul>"
        return render_template("index.html", name="处理失败", name_2="清空数据")


@app.route('/findtax', endpoint="findtax")  # 获取税金文件
# @time_call_one.stat_called_time
def find_tax_h5():
    src_path = 'D:/新建文件夹/WeChat Files/wxid_6xnvlbwhpof321/FileStorage/File/2020-06/'
    txt = "我要查税金"
    data = find_file_h5.run(src_path, txt)
    # return "处理成功" + "<ul><li><a href='/'>返回</a></li></ul>"
    return render_template("index.html", name=data, name_2="获取文件")


@app.route('/findchange', endpoint="findchange")  # 获取转换格式的文件
# @time_call_one.stat_called_time
def find_tax_h5():
    src_path = 'D:/新建文件夹/WeChat Files/wxid_6xnvlbwhpof321/FileStorage/File/2020-07/'
    txt = "我要转换"
    data = find_file_h5.run(src_path, txt)
    # return "处理成功" + "<ul><li><a href='/'>返回</a></li></ul>"
    return render_template("index.html", name=data, name_2="获取文件")


@app.route('/index')  # 首页
def index():
    return render_template('index.html', name_2="欢迎登陆")


@app.route('/search')  # 搜索
def search_index():
    return render_template('search2.html', name_2="番禺报价")


@app.route('/search=<name>', endpoint="search_1")  # 爬价格
@time_call_one.stat_called_time
def search_1(name):
    logging.info("ok")
    try:
        data = PaChong_qw.html1(name)

        return render_template('search2.html', name=data, name_2="番禺报价")
    except:
        return render_template('search.html', name="找不到商品", name_2="番禺报价")


@app.route('/test=<name>')  # 测试一个异步
def test(name):
    a=name
    executor.submit(test1)

    print("OK",a)
    return render_template('index.html', name="OK",name_2="欢迎登陆")

def test1():
    time.sleep(6)
    print("OKOK",date.datetime.now())






if __name__ == '__main__':
    executor = ThreadPoolExecutor(2) # 283行 测试一个异步


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

    app.run(host='127.0.0.1', port=5000, )
