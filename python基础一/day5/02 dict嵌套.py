
dict={
    "name":['alex','Wusir','taibai'],
    'py9':{
        'time':'1213',
        'learn_money':19800,
        'addr':'CBD'
    },
    'age':21
}

dict['age']=56
print(dict['name'])
dict['name'].append('ritian')
print(dict)

l=[1,2,'Wusir']
l[2]=l[2].upper()
print(l)
dict['name'][1]=dict['name'][1].upper()
print(dict)

female : 6
dict['py9']['female']=6
print(dict)


# fhdklah123rfdj12fdjsl3     '       123     12    13'
info=input('>>>>>').strip()
for i in info:
    if i.isalpha(): #判断字符是否为英文字符
        info=info.replace(i,' ')     #i为英文字母替换为空字符串

l=info.split()   #通过# 以空格为分隔符，包含 \n
print(l)
print(len(l))

# a='fhdklah123rfdj12fdjsl3'
# a.replace(1,'')
# print(a)