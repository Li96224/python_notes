
# 2、写函数，接收n个数字，求这些参数数字的和。
# def sum(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(sum(1,23,4,5))



# 3、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？

# a=10
#
# b=20
#
# def test5(a,b):
#     print(a,b)
#
# c = test5(b,a)  #这里传进去的实参是全局变量 b=20 a=10
# print(c)
#最终输入结果 20 10
#因为c=test(b,a) b=20 a=10 位置参数传进去 实参b=20=形参a 实参a=10=形参b
#test5函数里面最终打印a，b 所以输出结果为 a=20  b=10


# 4、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a=10
b=20
def test5(a,b):
    a=3
    b=5
    print(a,b)
c = test5(b,a)
print(c)

#输出结果是 3 5
#虽然c=test5(b,a) 在调用时已经传入了实参 但是函数test5里面也定义了同名变量 所以最终输出结果是3 5

#写函数，检查获取传入列表或元祖对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
# def func(l):
#     listvar=[]
#     for i in l:
#          if l.index(i) % 2 !=0 :
#              listvar.append(i)
#     return listvar
# print(func([1,2,3,4,5]))

# def func(l):
#     return l[1::2]
# print(func([1,2,3,4,5]))
#写函数，判断用户传入的对象（字符串，列表，元祖）长度是否大于5
# def Test(l):
#     if len(l)>5:
#         return "大于"
#     else:
#         return "小于"
# # print(Test("1234567"))
# def func(l):
#     return len(l)>5     #大于的话 结果为True 小于的话结果为False 这里的返回值满足为True不满足为false
# if func('123456'):      #if条件为真时执行下一步
#     print("大于")

#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并返回新内容给调用者
# def func(l):
#     listvar=[]
#     if len(l) > 2:
#         listvar.append(l[:2])
#     return listvar
# print(func([1,23,2]))

# def func(l):
#     if len(l) >2 :
#         return l[:2]
# print(func([1,2]))

#写函数，计算传入字符串中 数字，字母，空格以及其他的个数 并返回结果
# def func(l):
#     dict={"number":0,"letter":0,"blank":0,"else":0}
#     for i in l:
#         if i.isdigit():
#             dict["number"]+=1
#         elif i.isalpha():
#             dict["letter"]+=1
#         elif i.isspace():
#             dict["blank"]+=1
#         else:
#             dict["else"]+=1
#     return dict
# print(func('12ass 2211aaas qwqw/'))

# #写函数，检查用户传入的对象（字符串、列表、元祖）的每一个元素是否含有空内容，并返回结果
# def func(l):
#     for i in l:
#         if i == " ":
#             return True
#         else:
#             return False
# print(func("1 123 "))


# def func(x):
#     if type(x) is str and x:  #如果参数类型是字符串且字符串不能为空
#         for i in x:
#             if i == " ":
#                 return True
#     elif x and type(x) is list or type(x) is tuple: #参数是列表或者元祖
#         for i in x:
#             if not i:   #if条件判断i非正常数值时
#                 return True
#     elif not x:
#         return True
#
# print(func([1,' ']))

#写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# def func(dict):
#     for i in dict:              #循环遍历字典
#         if len(dict[i]) > 2 :   #dict[i]对应的是vaule的值
#             dict[i]=dict[i][:2] #通过切边的方式取前两位
#     return dict
# print(func({'k1':"121",'k2':"214555"}))


#写函数，接受两个数字参数，返回比较大的那个数字
# def func(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(func(1,5))

def func (a,b):
    return a if a>b else b      # 三元运算
print(func(5,3))

#三元运算
a=1
b=2
c = a if a>b else b         #如果a大于b 则返回a 否则返回b 再拿个变量c来接收 这种叫做三元运算
print(c)

# 变量 = 条件返回True的结果 if 条件 else 条件返回False的结果
#必须要有结果
#必须要有if和else
#只能是简单的条件判断

#写函数，用户传入修改的文件名，要修改的内容，执行函数，完成整个文件的批量修改操作

# def func(filename,old,new):
#     with open(filename, encoding='utf-8') as f, open('%s.bak'%filename, 'w', encoding='utf-8') as f2:
#         for line in f:
#             if old in line:  # 班主任:星儿
#                 line = line.replace(old,new)
#             # 写文件
#             f2.write(line)  # 小护士:金老板
#
#     import os
#     os.remove(filename)  # 删除文件
#     os.rename('%s.bak'%filename, filename)  # 重命名文件

# def func(filename,old,new):
#     当没有写打开方式时默认为r读
    # with open(filename, encoding='utf-8') as file, open('%s.bak'%filename, 'w', encoding='utf-8') as file1:
#         for line in file:
#             if old in line:
#                 line = line.replace(old, new)
#             # 写文件
#             file1.write(line)
#
#     import os
#     os.remove(filename)  # 删除文件
#     os.rename('%s.bak'%filename, filename)  # 重命名文件
#
# func()



#写一个函数完成三次登录功能，再写一个函数完成注册功能
# def func(username1,password1):
#     i=1
#     while i <=3:
#         username = int(input("请输入账号："))
#         password = int(input("请输入密码："))
#         if username1==username and password1==password:
#             return "登录成功"
#         else:
#             print(f"账号或密码错误还剩{3-i}次机会")
#         i+=1
# print(func(15007875118,123456))










