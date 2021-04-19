

li=[11,22,33,44,55,66,77,88,99]
#将大于66的存到key1 小于66存到key2 存到字典中
dict={}
listvar=[]
listvar1=[]
# for i in li:
#     if i == 66:
#         continue
#     if i > 66:
#         listvar.append(i)
#     else:
#         listvar1.append(i)
# dict.setdefault('key1',listvar)
# dict.setdefault('key2',listvar1)
# print(dict)

'''
输出商品列表，用户输入序号，显示用户选中的商品
    商品li=["手机",'电脑','鼠标垫','游艇']
要求:1：页面显示 序号 商品名称：
        1.手机
        2.电脑
    2:用户输入选择的商品序列号，然后打印商品名称    
    3：如果用户输入的商品序列号有误，则提升输入有误，并重新输入
    4：用户输入Q或者q 退出程序
'''
li=["手机",'电脑','鼠标垫','游艇']

while True:
    for i in li:
        print(li.index(i)+1,i)

    num_ber=input("请输入序号或输入Q或者q 退出程序：")
    if num_ber.isdigit():
        num_ber=int(num_ber)
        if num_ber>0 and num_ber<=len(li):
            print(li[num_ber-1])
        else:
            print("输入有误请重新输入")
    elif num_ber.upper()=="Q":
            break
    else:
        print("输入有误请重新输入")




