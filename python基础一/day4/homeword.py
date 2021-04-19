#
# 有变量name=' aleX leNb '完成以下操作
# 移除 name 变量对应的值两边的空格，并输出处理
name='aleX leNb'
print(name.strip(''))
# 移除 name 变量左边的'al'并输出结果处理
print(name.lstrip('al'))
# 移除 name 变量右边的'Nb'并输出结果处理
print(name.rstrip('Nb'))
# 移除 name 变量开头的a和最后的b
print(name.strip('a''b'))
# 判断 name 变量是否以'al'开头
print(name.startswith('ab'))
# 判断 name 变量是否以'Nb'作为结尾
print(name.endswith('Nb'))
# 将   name 变量对应的值中的 所有的'l'替换为P
print(name.replace('l','p'))
# 将第一个l替换为p
print(name.replace('l','p',1))
# 通过l分割
print(name.split('l'))
# 通过将第一个l分隔
print(name.split("l",1))
# 将变量大写
print(name.upper())
# 将变量小写
print(name.lower())
# 将变量首字母a大写
print(name.capitalize())
# 统计变量字母l出现的次数
print(name.count('l'))
# 统计变量前四位l出现的次数
print(name.count('l',0,4))
# 通过值N找出对应的索引 找不到返回-1
print(name.find("N"))
# 通过值N找出对应的索引 找不到就返回报错
print(name.index('N'))
# 找到X le 对应的索引
print(name.find('x le'))
# print(name.index('x'))
# 输出第二个字符
print(name[1])
# 输出前三个字符
print(name[2])
# 输出后两个字符
print(name[7::])
# 输入e对应的索引位置
#方法一：
listvar=[]
for i,j in enumerate(name):
    if j == 'e':
        listvar.append(i)
print(listvar)
#方法二：
print(name.find('e'),name.rfind('e'))
#方法三：
print(name.index('e'),name.rindex('e'))

#获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
name='oldboy'
print(name[:-1])

# （二）有字符串s1 = 'AlexBarrywusir '通过字符串索引或者切片得到以下结果：
# 1) s='Alex'
s1 = 'AlexBarrywusir '
print(s1[0:4])
# 2) s = 'exBarrywusir'
print(s1[2:])
# 3) s = 'AeB'
print(s1[0:5:2])
# 4) s = 'Axrw'
print(s1[0:10:3])
# 5) s = 'r'(最后一个r)
print(s1[-2])
# 6) s = 'aBxelA'
print(s1[-10::-1])
# 7) s = 'Be
print(s1[4:0:-2])

s='132a4b5c'
s1=s[0]+s[2]+s[1]
print(s1)

#计算请输入的数字的合 例如 5+9
#方法一
# content=input("请输入内容：")
# i=content.split("+")
# str=0
# for j in i :
#     print(j)
#     str=str+int(j)
# print(str)

# 方法二
# content=input("请输入内容：")
# index=content.find('+')
# a=int(content[:index])  #取+号之前的数
# b=int(content[index+1:])    #取+号之后的数
# print(a+b)

#统计输入的数字个数
# 方法一
# content=input("请输入内容：")
# listvar=[]
# for i in content:
#     if i.isdigit():
#         listvar.append(i)
# print(len(listvar))

# 方法二
# content=input("请输入内容：")
# sum=0
# for i in content:
#     if i.isdigit():
#         sum+=1
# print(sum)


# 遍历字符串逐个输出结果
#方法一
# s='asdef'
# for i in s:
#     print(i)

#方法二
# index=0
# while True:
#     print(s[index])
#     index+=1
#     if index==len(s):break