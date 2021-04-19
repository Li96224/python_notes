# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

# FLAG=False
# def login(func):
#     def inner(*args,**kwargs):
#         global FLAG
#         if FLAG==False:
#             username=input("输入账号:")
#             passwodr=input("输入密码:")
#             with open('Test.txt', mode='r+', encoding='utf-8') as file:
#                 listvar = file.readlines()
#                 listvar1 = listvar[0].split(" ")
#             if username==listvar1[0] and passwodr==listvar1[1]:
#                 print('登录成功')
#                 FLAG=True
#                 ret=func(*args,**kwargs)
#                 return ret
#             else:
#                 print("账号或密码错误")
#         else:
#             ret = func(*args, **kwargs)
#             return ret
#
#     return inner
#
# @login
# def shoplist_add():
#     print("增加")
#
# @login
# def shoplist_del():
#     print('删除一件物品')
#
# shoplist_add()
# shoplist_del()


#2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件

# import time
# def log(func):
#     def inner(*args,**kwargs):
#         with open('log',mode='a+',encoding='utf-8') as file:
#             file.write(func.__name__+'\n')
#         ret = func(*args, **kwargs)
#         return ret
#     return inner
#
# @log
# def shoplist_add():
#     print("增加")
#
# @log
# def shoplist_del():
#     print('删除一件物品')
#
# shoplist_del()
# shoplist_del()
# shoplist_add()



#1.编写下载网易内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
#2.为题目1编写装饰器，实现页面缓存功能
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

from urllib.request import urlopen
import os
def cache(func):
    def inner(*args,**kwargs):
        if os.path.getsize('web_cache.txt'):    #判断读取的文件内容非空时
            with open('web_cache.txt','rb') as  f:  #打开文件   因为文件内容编码为bytes二进制需要用b
                return f.read()                     #返回文件读取内容
        ret=func(*args,**kwargs)                #func函数等于get函数并将返回值赋值给ret
        with open('web_cache.txt','wb') as f:   #如果内容为空时 打开文件
            f.write(b'**************'+ret)      #将get函数的返回值存到文件中  因为文件内容编码为bytes二进制需要用b
        return ret                              #返回get函数的返回值
    return inner
@cache
def get(url):           #定义下载网页结果的函数
    code=urlopen(url).read()
    return code

ret=get('https://www.baidu.com/')
print(ret)
