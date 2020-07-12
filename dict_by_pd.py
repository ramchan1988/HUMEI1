'''
测试用 未封装
'''
import pandas as pd



d={'A':"1",'B':"1",'C':"1",'A1':"2",'B1':"2",'C1':"2"}

print(list(d.values()))
print(list(d.keys()))
d=pd.Series(list(d.keys()),list(d.values()))
d.index.name="ID"
d.name="data"
print(d)
print(d["1"].astype(str))

d.to_csv("data_test.csv")

data = pd.read_csv("data_test.csv")
print(data)
list = data.values.tolist()
index=data.index.tolist()

print(data.values.tolist())
image_id = []  # 存储的是要提取的数据
for i in range(len(list)):
    image_id.append(str(list[i][0])+": "+str(list[i][0]))
print(image_id)
image_id2=[str(list[i][0])+": "+str(list[i][1]) for i in range(len(list))]
print(image_id2)
