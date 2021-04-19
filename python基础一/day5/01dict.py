
#dict
'''
数据类型划分：可变数据类型，不可变数据类型
不可变数据类型：tuple（元祖） bool（布尔值） str（字符串） int
可变数据类型： dict（字典） list（列表） set（集合）
dict key 必须是不可变数据类型，可哈希，
    value：任意数据类型。
dict 优点：二分查找去查询
         存储大量的关系型数据
      特点：无序的
'''

dic = {
    'name':['大猛','小孟'],
    'py9':[{'num':71,'avg_age':18,},
           {'num': 71, 'avg_age': 18, },
           {'num': 71, 'avg_age': 18, },
           ],
    True:1,
    (1,2,3):'wuyiyi',
    2:'二哥',
}
print(dic)

dic1 = {'age': 18, 'name': 'jin', 'sex': 'male',}
#增
dic1['high']=185    #如果没有键值对，添加
dic1['age']=16      #如果键存在则会覆盖旧的

# dic1.setdefault('weight','222')   #有键值对，不会做任何改变 没有则会添加
# print(dic1)
# dic1.setdefault('weight',150)
# dic1.setdefault('name','111')
# print(dic1)

#删
# print(dic1.pop('age'))  #有返回值 按键去删除
# print(dic1)
# print(dic1.pop("weight",None))  #可设置返回值 #有找到key就返回被删除的值 没有就返回指定的返回值
# print(dic1)

# del dic1['name']
# print(dic1)
# del dic1    #直接删除变量dict的内存 找不到这个变量会报错
# print(dic1)

# dic1.clear()    #清空整个字典
# print(dic1)

#改  update
# dic1['age'] = 18
#
# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic2.update(dic)  #存在同名的key的值不会覆盖
#
# print(dic)
# print(dic2)

dic1 = {'age': 18, 'name': 'jin', 'sex': 'male',}
#查
print(dic1.keys(),type(dic1.keys()))    #打印key  返回的数据类型为元祖嵌套列表
print(dic1.values())                    #打印value 返回的数据类型为元祖嵌套列表
print(dic1.items())                     #打印key和value 返回的数据类型为列表嵌套元祖

for i in dic1:  #循环打印key
    print(i)

for i in dic1.keys():   #循环打印key
    print(i)

for i in dic1.values(): #循环打印value
    print(i)

# a,b=1,2
# print(a,b)

# a=1
# b=2
# a,b=b,a
# print(a,b)

a,b=[1,2],[2,3]
print(a,b)
a,b=(1,2)
print(a,b)

for k,v in dic1.items():    #打印key和value
    print(k,v)

v1=dic1['name']        #将key name对应的 value值 "jin"赋值给了变量v1
print(v1)

# v2=dic1['name1']  #找不到对应的key 会报错
# print(v2)

print(dic1.get('name1'))    #没有找到这个 key 'name1' 会返回None

print(dic1.get('name1','没有这个key'))  # 没有找到这个 key 'name1' 会返回设置的返回值
