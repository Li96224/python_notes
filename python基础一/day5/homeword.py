li=['alex', "wusir",'eric',"rain", 'rain']

# 计算列表长度并输出
print(len(li))
# 列表中追加元素“seven”，并输出添加后的列表
# li.append("seven")
# print(li)
# 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
# li.insert(0,"Tony")
# print(li)
# 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
# li[1]="Kelly"
# print(li)
# 请删除列表中的元素“eric”，并输出修改后的列表
# li.remove('eric')
# print(li)
# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
# print(li.pop(1))
# print(li)
# 请删除列表中的第3个元素，并输出删除元素后的列表
# li.pop[2]
# print(li)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del  li[1:5]
# print(li)
# 请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print(li)
# 请使用for、len、range输出列表的索引

# li=['alex', "wusir",'eric',"rain", 'rain']
# print(len(li))
# for i in range(len(li)):
#     print(i)
#     print(li[i])
# for i , j in enumerate(li):
#     print(i,j)

# 请使用enumrate输出列表元素和序号（序号从100开始）
# for i  , j in enumerate(li,100):
#     print(i,j)
# 请使用for循环输出列表的所有元素
# for i in li:
#     print(i)

#
list=[2,3,"k",['qwe',20,["k1",["tt",3,"1"]],89],'ab','adv']
#将列表lis中的'tt'变成大写（用两种方式）
# list[3][2][1][0]="TT"
# print(list)

# list[3][2][1][0]=list[3][2][1][0].upper()
# print(list)

#将列表lis中的数字3变成字符串100（用两种方式）


lis = [2,3,'k',['qwe',20,['k',['tt',3,'1']],89],'ab','adv']
'''
# 1)将列表lis中的’tt’变成大写（用两种方式）。
# lis[3][2][1][0] = "TT"
# print(lis)
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis2)
# 2)将列表中的数字3变成字符串’100’（用两种方式）。
# lis[1] = '100'
# lis[3][2][1][1] = '100'
# print(lis)
# lis[3][2][1].remove(3)
# lis[3][2][1].insert(1,'100')
# print(lis)
'''
# 3)将列表中的字符串’1’变成数字101（用两种方式）
# lis[3][2][1][2] = 101
# print(lis)
# lis[3][2][1][2] = int(lis[3][2][1][2].replace('1','101'))
# print(lis)
# print(lis[3][2][1][2])  # '1'
# lis[3][2][1][2] = int('10'+lis[3][2][1][2])
# lis[3][2][1][2] = int(lis[3][2][1][2]) + 100
# li = [1,2,3]
# li[2] = 33
# print(li)
# 5,查找列表li中的元素，移除每个元素的空格，
# 并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
# li = [‘taibai ’,’alexC’,’AbC ’,’egon’,’ Ritian’,’ Wusir’,’  aqc’]
li = ['taibai ','alexC','AbC ','egon',' Ritian',' Wusir','  aqc']
b=[]
# for i in li:
#     s=i.strip()
#     if (s.startswith("A")or s.startswith("a"))and s.endswith("c"):
#         b.append(s)
# for x in b:
#     print(x)

# for i in li:
#     s=i.strip()
#     if s[0].upper() == 'A' and s[-1] == 'c':
#         b.append(s)
# for x in b:
#     print(x)
# 6、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师","东京热",”武藤兰”,”波多野结衣”]
# 则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

# li=["苍老师","东京热","武藤兰","波多野结衣"]
# new_li= []
# info = input("评论")  # 苍老师，东京热 法律框架第三
# for i in li:
#     if i in info:
#         l = len(i)
#         info=info.replace(i,'*'*l)
# new_li.append(info)
# print(new_li)




