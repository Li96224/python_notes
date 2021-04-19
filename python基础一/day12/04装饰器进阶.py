


#带参数的装饰器
#500个函数
#设置全局变量根据变量值判断是否引用装饰器函数
# import time
# FLAGE=False
# def timmer_out(flag):
#     def timmer(func):
#         def inner(*args,**kwargs):
#             if flag:                    #如果flag为真则执行被装饰函数执行前后的代码
#                 start=time.time()
#                 ret=func(*args,**kwargs)
#                 end=time.time()
#                 print(end-start)
#                 return ret
#             else:                       #如果flag为假只执行被装饰的函数
#                 ret = func(*args, **kwargs)
#                 return ret
#         return inner
#     return timmer
#
# @timmer_out(FLAGE)   #timmer_out(FLAGE) =@timmer=wahaha=timmer(wahaha)
# def wahaha():
#     time.sleep(0.1)
#     print('11111')
#     return 'aaaaa'
#
# @timmer_out(FLAGE)
# def erguotou():
#     time.sleep(0.1)
#     print('222222')
#     return 'bbbbbb'
#
#
# print(wahaha())
# erguotou()


#多个装饰器装饰一个函数
#python核心编程


def wrapper1(func):
    def inner1():
        print('wrapper1 ,before func')
        ret = func()
        print('wrapper1 ,after func')
        return ret
    return inner1

def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')
        ret = func()
        print('wrapper2 ,after func')
        return ret
    return inner2

@wrapper2
@wrapper1       #取被装饰函数最近的一个装饰器
def f():
    print('in f')
    return '哈哈哈'

ret=f()
print(ret)


#
# def wrapper1(func):
#     def inner1():
#         print('wrapper1 ,before func')
#         ret = func()
#         print('wrapper1 ,after func')
#         return ret
#     return inner1
#
# def wrapper2(func):
#     def inner2():
#         print('wrapper2 ,before func')
#         ret = func()
#         print('wrapper2 ,after func')
#         return ret
#     return inner2
#
# def wrapper3(func):
#     def inner3():
#         print('wrapper3 ,before func')
#         ret = func()
#         print('wrapper3 ,after func')
#         return ret
#     return inner3
#
# @wrapper3
# @wrapper2
# @wrapper1       #f=wrapper1
# def f():
#     print('in f')
#     return '哈哈哈'
#
# print(f())


'''
wrapper3 ,before func   wrapper3中在被装饰的函数之前的代码
wrapper2 ,before func   wrapper2中在被装饰的函数之前的代码
wrapper1 ,before func   wrapper1中在被装饰的函数之前的代码
in f                    被装饰函数的代码
wrapper1 ,after func    wrapper1中在被装饰的函数之后的代码
wrapper2 ,after func    wrapper2中在被装饰的函数之后的代码
wrapper3 ,after func    wrapper3中在被装饰的函数之后的代码
哈哈哈                   
'''