

#装饰器形成的过程: 最简单的装饰器 有返回值的 有一个参数 万能参数
#装饰器的作用
#原则：开放封闭原则
#装饰器的固定模式


# import time
# print(time.time())  #获取当前时间
# time.sleep(10)      #代码跑到这个位置的时候暂停10秒

# def func():         #第一步定义函数func
#     time.sleep(0.1)
#     print('12345')
#
# def timmer(f):              #第二步定义装饰器函数   (因为第三步的调用此时的形参f的内存地址等同于函数func)
#     def inner():            #第四步执行inner函数
#         start=time.time()   #第八步
#         f()                 #第九步
#         end=time.time()     #第十步
#         print(end-start)    #第十一步
#     return inner        #返回inner函数的内存地址 #第五步返回inner函数
#
# func=timmer(func)       #第三步调用函数timer时将func作为实参传入了  第六步func等于返回值inner函数
# func()                  #第七步执行func函数


            # 语法糖
#
# def timer(f):               #装饰器函数
#     def inner():
#         start=time.time()
#         f()                 #被装饰的函数
#         end=time.time()
#         print(end-start)
#     return inner            #返回函数不用带()
#
#
# @timer                      #语法糖 @装饰器函数名      在被装饰的函数前面加上@装饰函数 起到的作用相当于func=timer(func)且这行代码可以不用写
# def func():                 #被装饰器的函数
#     time.sleep(0.01)
#     print("大家好")
# # func=timer(func)            #函数作为实参传入函数不用带()
# func()

#装饰器的作用：在不修改函数的调用方式，但是还想在原来的函数前后添加功能
#timer就是一个装饰器函数，只是对一个函数 有一些装饰作用

# 原则：开放封闭原则
# 开放：对扩展是开放的
# 封闭：对修改是封闭的


#装饰带参数函数的装饰器
# def timer(f):               #装饰器函数
#     def inner(*args,**kwargs):
#         start=time.time()
#         ret=f(*args,**kwargs)                 #被装饰的函数
#         end=time.time()
#         print(end-start)
#         return ret
#     return inner            #返回函数不用带()
#
#
# @timer                      #语法糖 @装饰器函数名
# def func(a,b):                 #被装饰器的函数
#     time.sleep(0.01)
#     print("大家好",a,b)
#     return '新年好'
#
#
# @timer                      #语法糖 @装饰器函数名
# def func1(a):                 #被装饰器的函数
#     time.sleep(0.01)
#     print("大家好",a)
#     return '新年好'
# # func=timer(func)            #函数作为实参传入函数不用带()
# ret=func(1,b=3)
# print(ret)



#
# def timer(f):        #装饰器函数
#     def inner(*args,**kwargs):
#         """在被装饰函数之前要做的事"""
#         ret=f(*args,**kwargs)       #被装饰的函数
#         """在被装饰函数之后要做的事"""
#         return ret
#     return inner
#
# @timer              #语法糖 @装饰器函数名
# def func(a,b):      #被装饰的函数
#     time.sleep(0.01)
#     print('666',a,b)
#     return '111'




# def wrapper(func):          #这时候传的的实参就是qqxing
#     def inner(*args,**kwargs):
#         ret=func(*args,**kwargs)    #被装饰的函数
#         return ret
#     return inner
#
# @wrapper        #qqxing等于wrapper(qqxing)
# def qqxing(a,b,c):
#     print(123,a,b,c)
#     return "112"
#
# # ret = qqxing()    #实际是执行inner
# qqxing(11,22,c=99)

def wrapper(func):
    def inner(*args,**kwargs):
        ret=func(*args,**kwargs)
        return ret
    return inner

@wrapper
def qqxing(*args,**kwargs):
    print("打印的值",*args,**kwargs)
    return "abc"
print(qqxing(1,23,3))