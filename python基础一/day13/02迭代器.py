
#迭代器
# l=[1,2,3]
# 索引取一个值 切片取多个值
# 循环取值  for while

# for i in l:
#     i
# for k in dic:
#     k

#可以循环的数据类型
# list
# dic
# str
# set
# tuple
# f=open()  #循环文件句柄
# range()   #range() 范围
# enumerate #枚举

print(dir([]))  #dir查询列表拥有的所有方法
#双下划线的方法叫做双下方法 已经写好的c语言的方法
# print([1].__add__([2]))
# print([1]+[2])
# 1 + 2 --> __add__ --> 3

# ret=set(dir([]))&set(dir({}))&set(dir(''))&set(dir(range(10)))
# print(ret)  #iterable
# print('__iter__' in dir(int))
# print('__iter__' in dir(bool))
# print('__iter__' in dir(list))
# print('__iter__' in dir(dict))
# print('__iter__' in dir(set))
# print('__iter__' in dir(tuple))
# print('__iter__' in dir(enumerate([])))
# print('__iter__' in dir(range(1)))


#只要能被for循环的数据类型 就一定拥有__iter__方法
# print([].__iter__())
#
# #一个列表执行了__iter__()之后的返回值就是一个迭代器
# print(dir([]))
# print(dir([].__iter__()))
# print(set(dir([].__iter__())) - set(dir([])))
# print([1,'a','bbb'].__iter__().__length_hint__())  #元素个数
# l = [1,2,3]
# iterator = l.__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# iterable 可迭代的 --> __iter__ #只要含有__iter__方法的都是可迭代的
# [].__iter__() 迭代器 --> __next__ #通过next就可以从迭代器中一个一个的取值

# 只要含有 __iter__方法的都是可迭代的 ————可迭代协议
# 迭代器协议————内部含有 __next__和__iter__方法的就是迭代器
# print('__iter__' in dir([].__iter__()))
# print('__next__' in dir([].__iter__()))
#
# from collections import Iterable    #Iterable可迭代
# from collections import Iterator    #Iterator迭代器
# print(isinstance([],Iterator))
# print(isinstance([],Iterable))

# class A:
#     def __iter__(self):pass
#     def __next__(self):pass
# a=A()
# print(isinstance(a,Iterator))
# print(isinstance(a,Iterable))

# 迭代器的概念
# 迭代器协议 ———— 内部含有__iter__和__next__方法的就是迭代器
# 可迭代协议 —————— 内部含有__iter__方法都是可迭代的

# 迭代器协议和可迭代协议
# 可以被for循环的都是可迭代的
# 可迭代的内部都是有 __iter__方法

# 只要是迭代器 一定可以迭代 因为迭代器包含 __iter__方法
# 可迭代的.__iter__()方法就可以得到一个迭代器
# 迭代器中的__next__()方法可以一个一个的获取值

#for循环其实就是在使用迭代器
# iterator
# 可迭代对象
# 直接给到内存地址
# print([].__iter__())
# print(range(10))


# for
# 只有是可迭代对象的时候 才能用for
# 当我们遇到一个新的变量，不确定能不能for循环的时候，就判断他是否可迭代

# for i in l:
#     pass
# iterator=l.__iter__()
# iterator.__next__()

#迭代器的好处:
    #从容器类型中一个一个的取值，会把所有的值都取到。
    #节省内存空间
        #迭代器并不会在内存中再占用一大块内存
        #而是随着循环 每次生成一个
        #每次next每次给我一个

# range
# f
# l=[1,2,3,4,6]
# iterator=l.__iter__()
# while True:
#     print(iterator.__next__())


# print(range(100000000000000000))
#
# print(list(range(0,3)))

# def func():
#     for i in range(20000000):
#         i='wahaha%s'%i
#     return i
#
# print(func())


# 生成器   ————> 迭代器
# 生成器函数 —— ——> 本质上就是我们自己写的函数
# 生成器表达式



# def reversal():









# inStr = "1234"
# # 把字符串转换成列表
# str_list = list(inStr)
# print(str_list)
# 用循环取出每一个元素
# for i in inStr:
#         index = str_list.index(i)
#
#         str_list.insert(index," ")
#
#         # 转换成字符串
#         outStr = "".join(str_list)
# print(outStr)



#编写一个函数提示用户输入四位整数，并反转显示输入的数字 （分割数字）
#例如输入：1234 输出 4 3 2 1

# def func():
#     strvar=input('输入四位整数：')     #定义字符串接收用户输入函数的整数
#     str_list=list(strvar[::-1])      #将字符串转换为列表赋值给新的变量
#     for i in strvar:                #遍历字符串遍历
#         print(i)
#         index=str_list.index(i)     #获取下标
#         print(index)
#         str_list.insert(index,' ')  #通过insert函数 通过下标添加空字符串
#         print(str_list)
#         outStr="".join(str_list)    #最后使用join函数以空字符串作为自定的字符 将str_list拼接成字符串 最后输入的结果就是 4 3 2 1
#     return outStr
#
# print(func())

str=" "         #定义空字符串
strvar='1234'
listvar=strvar[::-1]
listvar=str.join(listvar)
print(listvar)
#
#
# def func():
#     str=' '             #定义空字符串
#     strvar=input('输入四位整数：')     #定义字符串接收用户输入函数的整数
#     listvar = strvar[::-1]          #使用切片将字符串反转 listvar的数据类型为字符串
#     print(type(listvar),listvar)
#     listvar = str.join(listvar)     #再以空字符串为连接标志 将字符串连接起来
#     return listvar
# print(func())




print(*list(map(int,input("请输入一个四位整数:")))[::-1])
