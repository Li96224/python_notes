#元组 只读列表 可循环查询  可切片
#元组内嵌套非元组类型的数据可以改
tuplevar=(1,2,3,'alex',[2,3,4,'taibai'],'egon')
print(tuplevar[3])
print(tuplevar[0:4])
for i in tuplevar:
    print(i)
tuplevar[4][3]=tuplevar[4][3].upper()
print(tuplevar)
tuplevar[4].append('1')
print(tuplevar)
tuplevar[4][0]="22"
print(tuplevar)

s = 'alex'
s1='11'.join(s)
print(s1)
#列表转化为字符串 list--------->str     join
li=['taibai','alex','wusir','egon','女神',]
s='-'.join(li)
print(s)
#str---------------> list split()
print(s)

#range  [1,2,3,4,5,6,.......100........]

# for i in range(3,10):
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(0,10,3):
#     print(i)
# for i in range(10,0,-2):
#     print(i)
# for i in range(10,-1,2):    #不在范围就无法打印
#     print(i)


li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']
# for i in li:
#     if type(i) == list:
#         for j in i:
#             print("list",j)
#     else:
#         print("list1",i)


for i in range(len(li)):
    if type(li[i]) == list:
        for j in li[i]:
            print(j)
    else:
        print(li[i])
        