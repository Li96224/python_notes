# def max(a,b):
#     return a if a > b else b


def max(a,b):
    if a > b :
        return a
    else:
        return b

def the_max(x,y,z):     #函数的嵌套调用
    c=max(x,y)          #变量c等于函数max的返回值
    return max(c,z)     #函数max里面再传入了 变量c和第三个数

print(the_max(3,4,3))


#函数的嵌套定义
#内部函数可以使用外部函数的变量

a = 1
def outer():
    a=1
    def inner():
        b=2
        print(a)
        print('inner')
        def inner2():
            nonlocal a    #nonlocal声明了一个上层局部变量 (声明上层第一个找到的局部变量) （如果上层找不到的就报错）
            a+=1        #不可变数据类型的修改 只能影响到outer的局部变量a
            print('inner2')
        inner2()
    inner()
    print(a)    #这里打印的a是函数outer的局部变量 而不是全局变量a

outer()     #调用outer函数什么都没有输出 因为outer函数没有调用它里面的inner函数 他只是在outer函数里面定义了inner函数
print("全局",a)


# nonlocal 只能用于局部变量 找上层中离当前函数最近一层的局部变量
# 声明了nonlocal的内部函数的变量修改会影响到 离当前函数最近的一层的局部变量

# 对全局无效
# 对局部 也只是对 最近的 一层 有影响
# a = 0
# def outer():
#     # a = 1
#     def inner():
#         # a = 2
#         def inner2():
#             nonlocal a
#             print(a)
#         inner2()
#     inner()
#
# # outer()

# def func():
#     print(123)


# # func()  #函数名就是内存地址
# func2 = func  #函数名可以赋值
# func2()
#
# l = [func,func2] #函数名可以作为容器类型的元素
# print(l)
# for i in l:
#     i()

def func():
    print(123)

def wahaha(f):
    f()
    return f           #函数名可以作为函数的返回值

qqxing = wahaha(func)   # 函数名可以作为函数的参数
qqxing()

