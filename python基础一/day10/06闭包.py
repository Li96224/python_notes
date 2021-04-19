

#闭包：嵌套函数，内部函数调用外部函数的变量
# def outer():
#     a=1
#     def inner():
#         print(a)
#     print(inner.__closure__)    #输出(<cell at 0x0000016612941768: int object at 0x00007FF8E0B96290>,)
# outer()



# def outer():
#     a=1
#     def inner():
#         print(a)
#     return inner    #返回函数inner 不用带() 因为不是调用
# inn = outer()       #将函数outer的返回值赋值给变量inn 调用到这个变量的时候就就可以获得返回值inner
# inn()


# import urllib #导入模块


from urllib.request import urlopen
# ret=urlopen('https://www.baidu.com/').read()
# print(ret)



def get_url():
    url='https://www.baidu.com/'
    def inner():
        ret=urlopen(url).read()
        print(ret)
    return inner
get_func =  get_url()
get_func()