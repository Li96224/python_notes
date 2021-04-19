#简述变量名规范
'''
1.变量名可以使用数字/英文/下划线任意组合命名
2.不能与python自带的关键词重名
3.不能使用数字作为开头，以及不能使用中文/拼音
4.尽量做到见名识意的效果
5.使用规范命名 驼峰或下划线命名
'''

#name=input("") name的变量类型为字符串类型

# #计算 1 - 2 + 3-4+5-6 ... +99 中除了88意外所有数的总和
# 1-2+3-4+5-6
i=1
s=0
while i< 100:
    if i == 88:
        i+=1
        continue
    elif i % 2 ==1:
        s+=i
    elif i % 2 ==0:
        s-=i
    i+=1
print(s)

# #计算 1 - 2 + 3-4+5-6 ... -99 中除了88意外所有数的总和
i=1
j=-1
sum=0
while i <=99:
    if i == 88 :
        i+=1
        continue
    elif i % 2 == 0:
        sum-=i
    elif i % 2 == 1:
       if i!=99:
           sum+=i
       else:
           sum=sum+i*j
    i+=1
print(sum)