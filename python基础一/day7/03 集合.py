'''
集合：可变的数据类型 无效的 不重复的 里面的元素必须为不可变数据类型

'''

'''
set1=set({1,2,3})
# set2={1,2,3,[2,3],{'name':'alex'}}
print(type(set1),set1)          #<class 'set'> {1, 2, 3}
# print(type(set2),set2)        #set2里面包含列表和字典不符合语法报错
'''

set1 = {'alex','wusir','ritian','egon','barry',}
#增

#add
# set1.add('pp')
# print(set1)             #{'egon', 'ritian', 'wusir', 'alex', 'pp', 'barry'}

#update
set1.update('abc')      #迭代添加
print(set1)             #{'egon', 'b', 'a', 'ritian', 'wusir', 'alex', 'pp', 'c', 'barry'}
#
# #删除
#
# set1.pop()          #随机删除
# print(set1.pop())   #有返回值
# print(set1)
#
# set1.remove('alex')     #按元素值删除
# print(set1)
#
# set1.clear()            #清空
# print(set1)             #set()  空集合

# del set1
# print(set1)             #内存删除 查找不到这个变量set1

#查
for i in set1:
    print(i)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1 & set2  #求交集
print(set3)         #{4, 5}
print(set1.intersection(set2))  #{4, 5}


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 | set2)      #求并集    {1, 2, 3, 4, 5, 6, 7,8}

# print(set2.union(set1))  # {1, 2, 3, 4, 5, 6, 7}

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
# print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 - set2)  # {1, 2, 3}
# #set1独有的
# print(set1.difference(set2))  # {1, 2, 3}

# set1 = {1,2,3,}
# set2 = {1,2,3,4,5,6}
#
# print(set1 < set2)
# print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

# print(set2 > set1)
# print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。



#去重
li = [1,2,33,33,2,1,4,5,6,6]
# set1=set(li)
# print(set1)
# li=list(set1)
# print(li)

# li1=[]
# for i in li:
#     if i not in li1:
#         li1.append(i)
# print(li1)

dict=dict.fromkeys(li)
print(dict)
li=list(dict.keys())
print(li,type(li))

# s1={1,2,3}
# print(type(s1),s1)
#
#
# s = frozenset('barry')
# print(type(s),s)            #<class 'frozenset'> frozenset({'a', 'y', 'b', 'r'})
#
# for i in  s:
#     print(i)



