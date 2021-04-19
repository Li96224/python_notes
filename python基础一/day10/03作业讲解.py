#2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

# def func(l):
#     return l[::2]
# print(func([1,2,3,4,5,6]))
#
# def func1(l):
#     listvar=[]
#     for i in l:
#         if i % 2 !=0:
#             listvar.append(i)
#     return listvar
# print(func1([1,2,3,4,5,6]))


# 3、写函数，判断用户传入的值（字符串、列表、元组）长度是否大于5。

# def func(l):
#     if len(l)>5:
#         return "大于"
#     else:
#         return "小于"
# print(func([1,2,3,4,5,6]))

# 4、写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def func(l):
#     if len(l)>2:
#         return l[:2]
# print(func([1,2,3,4]))

# def f1(*p):
#     for i in p:
#         print(i)
#         l = len(i)
#         print(l)
#         if l > 2:
#             return(i[:2])
#         else:
#             return (i)
# ret = f1([11,22,33])
# print(ret)

# 5、写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果。

#定义函数
# def func(l):
#     #定义一个字典 key代表类型 vaule个数
#     dict={'num':0,'alphabet':0,'spacing':0,'else':0}
#     for i in l:     #循环遍历传进来的字符串
#         if i.isdigit():     #判断字符串为数字 字典dict对应的value则+1 （以下其他判断如下）
#             dict['num']+=1
#         elif i.isalpha():
#             dict['alphabet']+=1
#         elif i.isspace():
#             dict['spacing']+=1
#         else:
#             dict['else']+=1
#     return dict
# print(func("asdc121 1212/ sas"))


# 6、写函数，检查用户传入的对象（字符串、列表、元组）
# 的每一个元素是否含有空内容，并返回结果。

# def func(x):
#     if type(x) is str and x:
#         for i in x:
#             if i == ' ':
#                 return "字符串含义空格"
#     elif type(x) is list :
#         for i in x:
#             if i == " ":
#                 return "列表串含义空格"
#     elif type(x) is tuple :
#         for i in x:
#             if i == ' ':
#                 return "元祖含义空格"
#     else:
#         return False
# print(func((' ',1)))


#7、写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def func(dic):                  #定义函数
#     for k in dic:               #循环遍历形参
#         if len(dic[k]) > 2:     #通过dict[key]等于对应的value 判断vaule的长度是否大于2
#             dic[k] = dic[k][:2] #dict[key]通过切片修改dict[key]对应的值
#     return dic
# dic = {"k1": "v1v1", "k2": [11,22,33,44],'k3':[" "]}
# #ps：字典中的value只能是字符串或列表
# print(func(dic))

# 8、写函数，接收两个数字参数，返回比较大的那个数字。

# def func(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(func(3,2))

# def func(a,b):
#     return a if a > b else b
# print(func(5,1))

# 三元运算
# a = 1
# b = 5
# c = a if a>b else b   #三元运算
# print(c)

# 变量 = 条件返回True的结果 if 条件 else 条件返回False的结果
#必须要有结果
#必须要有if和else
#只能是简单的情况

# 9、写函数，用户传入修改的文件名，与要修改的内容，
# 执行函数，完成整个文件的批量修改操作（进阶）。
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
