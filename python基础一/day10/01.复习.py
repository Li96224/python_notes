# 函数
    # 可读性强 复用性强
# def 函数名():
      # 函数体
      #return 返回值
# 所有的函数 只定义不调用就一定不执行
            #先定义后调用

#函数名()   #不接收返回值
#返回值 = 函数名() #接收返回值

#返回值
    # 没有返回值 ：默认返回None
        # 不写return：函数内的代码执行完毕自动结束
        # 只写return：结束一个函数
        # return None

    # 返回一个值 ：结束了函数且返回一个值,可以是任意的值
    # 返回多个值 : 多个值之间用逗号隔开，接收的时候可以用一个变量接收（元祖），也可以用等量的多个变量接收

# def f(a):
#     return '栗子'
#
# ret = f('苹果')
# print(f('苹果'))

#参数
    #形参  定义函数的时候
        # 位置参数 ：必须传
        # *args ：动态参数 可以接收任意多个按位置传入的参数
        # 默认参数 ： 可以不传  —— 陷阱
        # **kwargs ： 动态参数 可以接受任意多个按关键字传入的参数
    #实参  调用函数的时候
        # 按照位置传参数
        # 按照关键字传参数
            # 可以混用 位置参数必须在关键字传参之前
            # 不能对一个参数重复赋值

# def 娃哈哈(*args):
#     print(args)
#
# # 娃哈哈(1,2,3,4)
# l = [1,2,3,4]
# 娃哈哈(*l)




