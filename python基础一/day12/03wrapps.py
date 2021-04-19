



from functools import wraps

                                #func=holiday
def wrapper(func):              # 1 定义装饰器函数
    @wraps(func)
    def inner(*args,**kwargs):  # 4 定义inner函数       #8执行inner函数
        print("被装饰的函数执行前")                      # 9
        ret=func(*args,**kwargs)                       #10执行func函数因为第三步的原因 此时func等于holiday函数
        print("被装饰的函数执行后")                      #13
        return ret                                     #14返回ret
    return inner                # 5 返回inner函数

@wrapper        #holiday=wrapper(holiday)   #2使用装饰器函数 3调用wrapper函数并将holiday函数作为实参传入wrapper函数  6变量名holiday接收返回值inner函数
def holiday(day):
    '''这是一个放假通知'''
    print(f'天数{day}')                       #11
    return 1                                 #12将返回值1赋值给ret

ret=holiday(3)                          #7调用holiday函数并传入实参3 此时的holiday函数内存地址等于inner函数  15将ret的返回值赋值给了ret
print(ret)                                  #16 打印

print(holiday.__name__)
print(holiday.__doc__)


# def wahaha():
#     '''
#     一个打印哇哈哈的函数
#     :return:
#     '''
#     print('哇哈哈')
# print(wahaha.__name__)  #查看函数名
# print(wahaha.__doc__)   #document 查看函数的注释




