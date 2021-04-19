#复习

#讲作业


#装饰器的进阶
    #functools. wraps
    #带参数的装饰器
    #多个装饰器装饰同一个参数


#周末的作业
    #文件操作
    #字符串处理
    #输入和输出
    #流程控制


# 装饰器
# 开放原则： 开放封闭原则
# 装饰器的作用：在不改变原函数的调用方式的情况，在函数的前后添加功能
# 装饰器的本质：闭包函数 （内部函数调用外部的变量）



def wrapper(func):       #第一步定义装饰器函数
    def inner(*args,**kwargs):  #第四步走到inner函数
        ret=func(*args,**kwargs)
        return ret
    return inner                #返回inner函数

@wrapper  #holiday=wrapper(holiday) #第三步 wrapper(holiday) 调用函数wrapper将holiday作为实参传入wrapper
def holiday(day):       #第二步定义被函数
    print(f"假期天数{day}")
    return "开心"
ret=holiday(1)
print(ret)



#
# def warpper(f):
#     def inner(*args,**kwargs):
#         print('在被装饰器的函数执行之前做的事')
#         ret = f(*args,**kwargs)
#         print('在被装饰器的函数执行之后做的事')
#         return ret
#     return inner
#
# @warpper  #func=warpper（func）
# def func(a,b,c=1):
#     print('123')
#     return a,b,c
#
# print(func(1,23,4))

# ret=func(11,22,33)
# print(ret)



def outer(*args,**kwargs):
    print(args)
    print(*args)
    def inner(*args):
        print("inner:",args)
    inner(*args)
outer(1,2,3,4)      #==outer(*[1,2,3,4])  #==outer(*(1,2,3,4))  参数前面加个*号解包裹







