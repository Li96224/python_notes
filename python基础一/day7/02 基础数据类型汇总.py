
#
# listvar=[1,2,3,4,5,6]
# print(len(listvar))
#
# for i in range(len(listvar)):
#     print(i)
#     print(listvar[i])

#包含有字符串k的键操作删除 包括key:value
dictvar={"k1":"vi","k2":"v2","v1":"v2"}

#第一种
# dictvar1={}
# for i in dictvar.keys():
#     if "k" not in i:
#         dictvar1.setdefault(i,dictvar[i])
# print(dictvar1)


#第二种
# l=[]
# for i in dictvar:
#     if "k" in i:
#         l.append(i)
#
# print(l)
# for i in l:
#     del dictvar[i]
# print(dictvar)

'''
listvar=[1,2,3,4,5,6,7]
for i in range(len(listvar)):
    print(i)            #初始值i=0                 初始值i=1
    del listvar[i]      #操作删除后 listvar的下标会发生变化
    print(listvar)      #[2, 3, 4, 5, 6, 7]        [2, 4, 5, 6, 7]
'''

#
# #取步长间隔为2
#第一种
# listvar=[1,2,3,4,5,6,7]
# listvar=listvar[::2]    #listvar[::2] 赋值给listvar
# print(listvar)


#第二种
# listvar1=[]
# for i in listvar:
#     if  listvar.index(i) %  2 == 0:
#         listvar1.append(i)
# listvar=listvar1
# print(listvar)

# lis = [11,22,33,44,55]
# for i in range(len(lis)-1,-1,-1):
#     print(i)
#     if i % 2 == 1:
#         print(i)
#         del lis[i]
#         print(lis)
# print(lis)



dict=dict.fromkeys([1,2,3],'春哥')
print(dict)     #{1: '春哥', 2: '春哥', 3: '春哥'}


dict=dict.fromkeys([1,2,3,],[])
print(dict)     #{1: [], 2: [], 3: []}

dict[1].append("kk")
print(dict)     #{1: ['kk'], 2: ['kk'], 3: ['kk']}

dict[2].extend("pp")    #迭代添加
print(dict)

l1=[]
l2=l1
l3=l1

l3.append('a')
print(l1,l2,l3)

#转换bool值
''' 
0或空值 为false
非0、非空的值为True    

'''

#元祖 如果元祖里面只有一个元素且不加逗号，那么元素是类型类型 变量就是什么类型
t1=(1)
t2=(1,)
print(t1,t2,type(t1),type(t2))      #1 (1,) <class 'int'> <class 'tuple'>


tu1=([1])
tu2=([1],)
print(tu1,tu2,type(tu1),type(tu2))  #[1] ([1],) <class 'list'> <class 'tuple'>

dict=dict.fromkeys([1,2,3,],3)
print(dict)
dict[1]=4
print(dict)