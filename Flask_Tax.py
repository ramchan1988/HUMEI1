
from flask import Flask
import Tax
import movefile

app = Flask (__name__)
@app.route('/')
def hello() -> str:
    ADD = "E:/HUMEI/Excel_shunxu/税金/"
    src_path = 'D:/新建文件夹/WeChat Files/ramchan1988/FileStorage/File/2020-06/'
    txt = "我要查税金"
    movefile.run(src_path,ADD,txt)
    print(Tax.tax_main_(ADD))
    return Tax.tax_main_(ADD)


app.run()
