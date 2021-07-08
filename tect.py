import numpy as np
import pandas as pd
np.set_printoptions(threshold = 1e6)
df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008],
    "gender":['male','female','male','female','male','female','male','female'],
    "pay":['Y','N','Y','Y','N','Y','N','Y',],
    "m-point":[10,12,20,40,40,40,30,20]})
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
                   "date":pd.date_range('20130102', periods=6),
                   "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age":[23,44,54,32,34,32],
                   "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
                   "price":[1200,np.nan,2133,5433,np.nan,4432]},
                   columns =['id','date','city','category','age','price'])
df['city']=df['city'].replace('SH','shanghai')
print(df)
df_inner=pd.merge(df,df1,how='inner')
print(df_inner)
# df_left=pd.merge(df,df1,how='left')
# print(df_left)
# df_right=pd.merge(df,df1,how='right')
# print(df_right)
# df_outer=pd.merge(df,df1,how='outer')
# print(df_outer)
# df_inner=df_inner.set_index('id')
# print(df_inner)
df_inner=df_inner.sort_values(by=['age'])
print(df_inner)
df_inner=df_inner.sort_index()
print(df_inner)
df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')
print(df_inner)
split=pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size'])
df_inner=pd.merge(df_inner,split,right_index=True, left_index=True)
print(df_inner)
print(df_inner.loc[0:1])
print(df_inner.reset_index())
df_inner=df_inner.set_index('date')
# print(df_inner[:'2013-01-04'])
# print(df_inner.iloc[:3,:2])
# print(df_inner.iloc[[0,2,5],[4,5]])
print(df_inner['city'].isin(['shanghai','Beijing']))
print(df_inner['city'].replace(' ',''))
print(df_inner.loc[df_inner['city'].isin(['shanghai','Beijing'])])


list1 = ["小张","小王","小李"]
print("---增加前列表数据----")
for list in list1:
    print(list)

# addname = input("请输入添加的学生姓名：")
# list1.append(addname)     #append为在末尾追加一个元素

print("---增加后列表数据----")
for list in list1:
    print(list)
'''

'''
a = [1,2]
b = [3,4]
a.append(b) #将列表当做一个元素加入到列表中
print(a)
a.extend(b) #将列表中的每个元素逐一追加到列表中
print(a)

# import random
# offices = [[],[],[]]
# names = ["A","B","C","D","E","F","G","H"]
# for name in names:
#     index = random.randint(0,2)  #注意这是左闭右闭
#     offices[index].append(name)
#
# i = 1
# for office in offices:
#     print("办公室%d的人数为：%d"%(i,len(office)))
#     i +=1
#     for name in office:
#         print("%s"%name,end="\t")
#         print("\n")
#         print("-"*28)
#
# #元组：增(连接)
# tup1 = (12,34,56)
# tup2 = ("abc","xyz")
# tup = tup1 + tup2
# print(tup)


# #元组：删
# tup1 = (12,34,56)
# print(tup1)
# del tup1 #删除了整个元组变量
# print("删除后：")
# print(tup1)


# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

a = 100
def te1():
    a = 300    #局部变量优先使用
    print("te1--------修改前：a = %d"%a)
    a = 200
    print("te1--------修改后：a = %d"%a)

def te2():
    print("te2--------：a = %d"%a) #没有局部变量，默认使用全局变量
te1()
te2()


a = 100
def te1():
    global a   #声明全局变量在函数中的标识符
    print("te1--------修改前：a = %d"%a)
    a = 200
    print("te1--------修改后：a = %d"%a)

def te2():
    print("te2--------：a = %d"%a) #没有局部变量，默认使用全局变量
te1()
te2()

try:
    print("------test-----1----")
    f = open("123.txt", "r")
    print("------test-----2----")
    print(num)
except (NameError,IOError) as result: #捕获异常内容
    print("产生错误了")
    print(result)