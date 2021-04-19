

# usename=input("请输入账号：")
# password=input("请输入账号密码：")
#
# with open("lis_info",mode='w+',encoding="utf-8") as file:
#     file.write("{}\n{}".format(usename,password))
# print('注册成功')


i=1

while i<=3:
    use = input("请输入账号：")
    pas = input("请输入账号密码：")
    with open("lis_info",mode='r+',encoding="utf-8") as file1:
        listvar=file1.readlines()       #换行输出
        # print(listvar)                #输出数据类型为list
        if use==listvar[0].strip() and pas==listvar[1].strip(): #strip去掉换行符
            print('登录成功')
            break
        else:
            print("账号或密码错误请重新登录")
    i+=1

