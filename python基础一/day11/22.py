#
#
# import time
# # print(time.time())  #获取当前时间
# # time.sleep(10)
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


def outer():
    def inner():
        return 'inner'
    ret=inner()
    return ret
print(outer())