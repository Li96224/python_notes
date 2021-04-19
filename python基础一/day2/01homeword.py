#1、使用while循环输入12345678910

# i=1
# sum=0
# while i <=10:
#     sum+=1
#     print(sum)
#     i+=1
#

##1、使用while循环输入123456   8910
# i=0
# while i <10:
#     i+=1
#     if i==7:
#         print('')
#     else:print(i)

##1、使用while循环输入1234568910
# i=0
# while i <10:
#     i+=1
#     if i!=7:
#         print(i)



#2、求1-100的所有数的和
# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

#3、输出1-100内的所有奇数

# i=1
# while i<=100:
#     if i % 2 !=0:
#         print(i)
#     i+=1


#3、输出1-100内的所有偶数
# i=1
# while i<=100:
#     if i % 2 ==0:
#         print(i)
#     i+=1

#4、输出1-99所有数的和
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


# a=""
# print(bool(a))

#5、求1-2+3-4+5-6 ... 99的所有数的和
#2 4 6 8 10 12 之类的数为偶数 为偶数时就相减
#1 3 5 7 9 11  为奇数 为奇数时就相加
sum=0
i=1
while i<100:
    if i % 2==0:
        sum-=i
    elif i % 2 !=0:
        sum+=1
    i+=1
print(sum)


sum = 0
count = 1
while count < 100:
    if count % 2 == 0:
        sum = sum - count
    else:
        sum = sum + count
    count += 1
print(sum)