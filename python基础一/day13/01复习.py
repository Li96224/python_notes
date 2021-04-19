


#函数 -----2天
    # 函数的定义和调用
    # def函数名(形参)
        #函数体
        #return 返回值
    #调用 函数名(实参)
    # 站在形参的角度上：位置参数，*args,默认参数,**kwargs
    # 站在实参的角度上：按位置传参，按照关键字传
    # 返回值：没有返回值 返回一个值 返回多个值
    # 接受返回值：没有返回值不接收，返回一个值用一个变量接收，返回多个值用一个变量或对应数目的变量接收

#闭包函数——————在内部函数引用外部函数的变量
#装饰器————装饰器一定是闭包函数
    #装饰器的作用：在不改变原来函数的的调用方式的情况下，在这个函数的前后添加新功能
    #完美的符合了一个开发原则：开放封闭原则
        # 对扩展是开放的
        # 对修改是封闭的
    #基础的装饰器
        # from  functools import wraps
        # def wrapper(func):
        #      @wraps(func)         #可以还原被装饰函数原本的内存地址（函数名）
        #     def inner(*args,**kwargs):
        #         '''在函数被调用之前添加的代码'''
        #         ret=func(*args,**kwargs)      #func是被装饰的函数 在这里被调用
        #         '''在函数被调用之后添加的代码'''
        #         return ret
        #     return inner
        #  @wrapper 被装饰的函数名前使用装饰器
        #    def func():
        #         pass
        #    func.__name__  函数名.__name__ 查询函数名
# 带参数的装饰器
# @wrapper -- > @warapper(argument)
# 三层嵌套函数
# def outer(形参):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             '''在函数被调用之前添加的代码'''
#             ret = func(*args,**kwargs)   # func是被装饰的函数 在这里被调用
#             '''在函数被调用之后添加的代码'''
#             return ret
#         return inner
#     return wrapper
# @outer(True)
# def func():
#     pass

    #多个装饰器装饰一个函数
        #俄罗斯套娃
from functools import wraps
def wrapper1(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print('before 1')
        print('******')
        ret = func(*args,**kwargs)   # func是被装饰的函数 在这里被调用
        '''在函数被调用之后添加的代码'''
        return ret
def wrapper2(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print('before 2')
        ret = func(*args,**kwargs)   # func是被装饰的函数 在这里被调用
        '''在函数被调用之后添加的代码'''
        return ret
@wrapper1
@wrapper2      
def func():
  print('111')







