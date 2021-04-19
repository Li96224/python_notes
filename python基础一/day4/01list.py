# li = ['alex',[1,2,3],'wusir','egon','女神','taibai']
# l1=li[0]
# print(l1)
# l2=l1[1]
# print(l2)
# l3=l1[0:3]
# print(l3)


# li = ['alex','wusir','egon','女神','taibai']

#增加 append(末尾追加元素) insert（通过下标添加元素） extend(末尾追加多个元素的值的序列)
# li.append('日天')
# li.append(1)
# print(li)

# while True:
#     username=input('>>>')
#     if username.strip().upper() == "Q":
#         break
#     else:
#         li.append(username)
# print(li)
# li.insert(4,'拉拉')
# print(li)
# li.extend('小小')
# li.extend([1,2,3])
# print(li)

#删 pop（默认删除末尾元素 传入下标时删除对应的元素） remove（通过元素的值删除第一个元素） del（可通过索引范围删除元素）
li = ['taibai','alex','wusir','egon','女神',]
# print(li.pop())     #有返回值
# print(li.pop(1))
# print(li)
#
# li.remove("taibai")
# print(li)
#
# li.clear()  #清空
# print(li)

# del li[0:2]
# print(li)

#改 通过下标修改对应的下标的值
li[0]='666'
print(li)
#切片
li[0:3]="1111222333"
print(li)

li[0:3]="123",'234','456'
print(li)

#查  通过下标 切片 find(不能用于列表)  index（第一个值返回索引）
for i in li:
    print(i)
print(li[0:2])

#公共方法
listvar=[1,2,2,4,5,6]
print(len(listvar))
print(listvar.count(2))
print(listvar.index(4))

#正向排序
li.sort()   #默认为reverse=False  list.sort( key=None, reverse=False)
print(li)
#反向排序
li.sort(reverse=True)
print(li)
#反转
li.reverse()
print(li)

#列表嵌套列表
li = ['taibai','武藤兰','苑昊',['alex','egon',89],23]

# print(li[1][1])
# name = li[0].capitalize()
# # print(name)
# li[0] = name
# li[0] = li[0].capitalize()
# li[2] = '苑日天'
# print(li[2].replace('昊','ritian'))
# li[2] = li[2].replace('昊','ritian')
# li[3][0] = li[3][0].upper()
# print(li)
