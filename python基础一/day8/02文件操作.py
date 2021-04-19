
#读

#创建一个文件对象 或者 是句柄 （文件以什么编码格式保存 encoding格式 就用什么打开）
# f=open(r'D:\淘宝课程笔记\python基础一\day8\new 1','r',encoding='utf-8')
#
# content=f.read()    #读文件 有返回值
# print(f,type(f))      #打印返回值（文件内容）  变量的类型为字符串
# print(content,type(content))    #类型为句柄 特殊对象
# f.close()           #关闭文件


# f=open(r'D:\淘宝课程笔记\python基础一\day8\new 1',mode='rb') #rb以二进制方式操作文件 不接受编码类型
#
# content=f.read()    #读文件 有返回值
# print(content)      #打印返回值（文件内容）
# f.close()           #关闭文件


#读写
#r+ 读写 先读后写 读完后光标在末尾 写入的字符就在末尾 读写完后 再读的话也只会读一遍
# f=open('log',mode='r+',encoding='utf-8')
# print(f.read())
# f.write('7777')
# print(f.read())
# f.close()

#r+ 读写模式下 先写后读的话 不会追加 只能覆盖 写入的内容多少位就会符合原有内容的多少位 写入的字符长
# 度超过内容里面原有的话则直接覆盖完了就没有了
# f=open('log',mode='r+',encoding='utf-8')
# f.write('aaaaaaaa')
# print(f.read())
# f.close()

#r+b bytes 二进制文件 文件传输之类的
# f=open('log',mode='r+b')
# print(f.read())
# f.write('7777'.encode('utf-8'))
# f.close()


#写

#对于写w：没有此文件就会创建文件
# f=open(r'log','w',encoding='utf-8')
# content=f.write('高清')    #写入文件 写入的类型必须为str
# print(f,type(f))      #打印返回值（文件内容）  变量的类型为字符串
# print(content,type(content))    #类型为句柄 特殊对象
# f.close()           #关闭文件

# #文件存在时 先将源文件的内容全部清除，在重新写入
# f=open('log',mode='w',encoding='utf-8')
# f.write('附件坎坎坷坷')
# f.close()

#w 二进制文件写入
# f=open('log',mode='wb')
# f.write('啦啦啦啦啦'.encode('utf-8'))    #模式为'wb'时 写入的数据需转为utf-8 才能接收
#                                         #编码方式需要与文件本身的编码方式一致才能写入
# f.close()

#写读 w+ 只要有w都先清除再写 写完后光标处于末尾的话没有数据可读了
# f=open('log',mode='w+',encoding='utf-8')
# f.write('附件坎坎坷坷12345')
# f.seek(0)   #seek 调节光标的位置
# print(f.read())
# f.close()


#追加

# f = open('log',mode='a',encoding='utf-8') #追加位置到文件内容光标后面
# f.write('aaa')
# f.close()

# f = open('log',mode='ab')
# f.write('aaa'.encode('utf-8'))
# f.close()

# #a+ 追加读
# f = open('log',mode='a+',encoding='utf-8') #追加位置到文件内容光标后面
# f.write('aaa')
# f.seek(0)
# print(f.read())
# f.close()



#功能详解


# f=open(r'log',mode='r',encoding='utf-8') #rb以二进制方式操作文件 不接受编码类型
# # content=f.read(3)    #read可以传参设置读取字符范围 读出的都是字符
# f.seek(3)               #三个字节 seek按字节去定光标位置
# print(f.tell())         #获取当前文件光标的位置
# content=f.read()
# print(content)
# f.close()



f = open('log',mode='r+',encoding='utf-8') #追加位置到文件内容光标后面
                                # 可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
# f.write('aaa')
# count=f.tell()
# print(count)
# f.seek(count-9)
# print(f.read())
# line=f.readline()       #一行一行的读 读出来的数据类型为字符串
# line=f.readlines()      #每一行当初列表中的一个元素，添加到list中
# l1=f.truncate()
# print(l1)
#
# for line in f:
#     print(line)
# f.close()

#with open 默认执行完后会关闭文件不需要些close 且可以打开多个文件
with open('log',mode='r+',encoding='utf-8') as  file , open(
    'log',encoding='utf-8',mode='r+'
)  as file1:
    print(file.read())