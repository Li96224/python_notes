

#1、使用while循环输入12345678910

# i=1
# sum=0
# while i <=10:
#     sum+=1
#     i+=1
#     print(sum)
#
# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=1
# sum=0
# while i <=10:
#     sum+=1
#     print(sum)
#     i+=1
#

# i=1
# while i <=10:
#     print(i)
#     i+=1

#2、求1-100的所有数的和
# i=1
# sum=0
# while i<=100:
#     sum=i+sum
#     i+=1
# print(sum)
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)
# i=1
# sum=0
# while i <=100:
#     sum+=i
#     i+=1
# print(sum)

#3、输出1-100内的所有奇数
# i=1
# while i<=100:
#     if i % 2 !=0:
#         print(i)
#     i+=1
#
# for i in range(1,101):
#     if i % 2 !=0:
#         print(i)


# i=1
# while i<=100:
#     if i % 2 !=0:
#         print(i)
#     i+=1

#3、输出1-100内的所有偶数


# for i in range(1,101):
#     if i % 2 ==0:
#         print(i)

# i=1
# while i<=100:
#     if i % 2 ==0:
#         print(i)
#     i+=1

#4、输出1-99所有数的和
sum=0
for i in range(1,100):
    sum+=i
print(sum)

# i=1
# sum=0
# while i <100:
#     sum+=i
#     i+=1
# print(sum)

#5、用户登录（三次机会）

# user='admin'
# passw='admin'
# i=1
# while i<=3:
#     username=input("请输入用户名：")
#     password=input("请输入密码：")
#     if username==user and password==passw:
#         print('登录成功')
#         break
#     elif 3-i==0:
#         print("结束了")
#     elif 3-i>0:
#         print(f'账号或密码错误，还要{3-i}次机会')
#     i+=1

# -*- encoding:utf-8 -*-
# print('我爱中国')
'''
x = 1+2+3+4
print(x)
print(x*5)
y = x*5
print(y+100-45+2)

print('泰哥泰哥，我是小弟')
print('泰哥泰哥，我是三弟小妹')


t-t = 2
3t_t = 23
*r = 4
_ = 'fdsa'
___ = 4
%- = 'fdsa'
2w = 5
qwe-r = 'wer'

kfdsdlafhsdakfhdsakdfjkhsdakf = '太白'
print(名字)
AgeOfOldboy = 56

NumberOfStudents = 80

#下划线

age_of_oldboy = 56

number_of_students = 80


age1 = 12
age2 = age1
age3 = age2
age2 = 100
age3 = 5
print(age1,age2,age3) #12, 100 ,100
					  #12,12,12,
					  #12,100,12
					  #100,100,100,

print(100,type(100))
print('100',type('100'))

print(1)
print("jsdfdsfsadl;fjdsal;j")
print("I'm a teacher")


a = '泰哥'
b = '小二'
c = a + b
print(c)
print('泰哥' + '小二' +'货')

print('坚强'*8)


msg = """
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
"""
#print(msg)
print(True,type(True))
print('True',type('True'))

name = input('请输入你的名字：')
age = input('请输入你的年龄：')
print('我的名字是'+name,'我的年龄'+age+'岁')
'''
# 第一种：
'''
if 4 > 5 :
	print('我请你喝酒')
print('喝什么酒')

#第二种：
if 4 > 5:
	print('我请你喝酒')
else:
	print('喝什么酒')
'''

'''
#多选：
num = input('请输入您猜的数字：')

if num == '1':
	print('一起抽烟')
elif num == '2':
	print('一起喝酒')
elif num == '3':
	print('新开了一家，走看看')
else:
	print('你猜错了.....')


score = int(input("输入分数:"))

if score > 100:
    print("我擦，最高分才100...")
elif score >= 90:
    print("A")
elif score >= 60:
    print("C")
elif score >= 80:
    print("B")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")

name = input('请输入名字：')
age = input('请输入年龄：')

if name == '小二':
	if age == '18':
		print(666)
	else:
		print(333)
else:
	print('错了....')
'''

# while
'''
print('111')
while True:
	print('我们不一样')
	print('在人间')
	print('痒')
print('222')
'''
# 从1--100
'''
count = 1
flag = True
#标志位
while flag:
	print(count)
	count = count + 1
	if count > 100 :
		flag = False



count = 1
while count <= 100:
	print(count)
	count = count + 1


count = 1
sum = 0

while count <= 100:
	sum = sum + count 
	count = count + 1

print(sum)
'''

# break
'''
print('11')
while True:
	print('222')
	print(333)
	break
	print(444)
print('abc')

count = 1
while True:
	print(count)
	count = count + 1
	if count > 100:break




print(111)
count = 1
while count < 20 :
	print(count)
	continue
	count = count + 1
'''

# count = 0
# while count <= 100:
#     count += 1
#     if count > 5 and count < 95:
#         continue
#     print("loop ", count)
#
# print("-----out of while loop ------")



"""
1，计算机基础。
2，python历史。

	宏观上：python2 与 python3 区别：
		python2 源码不标准，混乱，重复代码太多，
		python3 统一 标准，去除重复代码。
3，python的环境。

	编译型：一次性将所有程序编译成二进制文件。
		缺点：开发效率低，不能跨平台。
		优点：运行速度快。
		：C，C++等等。
	
	解释型：当程序执行时，一行一行的解释。
		优点：开发效率高，可以跨平台。
		缺点：运行速度慢。
		:python ,php,等等。
	
4，python的发展。
5，python种类。

运行第一个py文件：
	python3x :python 文件路径 回车
	python2x :python2 文件路径 回车
	python2 python3 区别：python2默认编码方式是ascii码
						  解决方式：在文件的首行：#-*- encoding:utf-8 -*-
						  python3 默认编码方式utf-8

						  
6，变量。
	变量：就是将一些运算的中间结果暂存到内存中，以便后续代码调用。
	1,必须由数字，字母，下划线任意组合，且不能数字开头。
	2，不能是python中的关键字。
	['and', 'as', 'assert', 'break', 'class', 'continue',
	'def', 'del', 'elif', 'else', 'except', 'exec',
	'finally', 'for', 'from', 'global', 'if', 'import', 
	'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 
	'raise', 'return', 'try', 'while', 'with', 'yield']
	3，变量具有可描述性。
	4,不能是中文。
7，常量。
	一直不变的量。     π
	BIR_OF_CHINA = 1949
	
	
8，注释。
方便自己方便他人理解代码。
单行注释：#
多行注释：'''被注释内容'''  


9，用户交互。input
   1，等待输入，
   2，将你输入的内容赋值给了前面变量。
   3，input出来的数据类型全部是str
   



10，基础数据类型初始。
数字：int 12,3,45 
    + - * / ** 
	% 取余数
	ps:type()
		字符串转化成数字：int(str) 条件：str必须是数字组成的。
		数字转化成字符串：str(int)
字符串：str，python当中凡是用引号引起来的都是字符串。
	可相加:字符串的拼接。
	可相乘：str * int
bool:布尔值。 True False。


11，if。

if 条件:
	结果
	





12，while。

while 条件:
	循环体
	无限循环。
	终止循环：1，改变条件，使其不成立。
			  2,break

	continue
	


"""








