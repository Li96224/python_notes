

#文件处理
    #打开文件
        #open('路径'，'打开方式',指定编码方式)
        #打开方式 r w a r+ w+ a+
            #r+ 打开文件直接写和读完再写 两者的区别是先读再写光标会乱。（建议直接r/w/a）
        #编码方式 常规使用utf-8
    #操作文件
        #读
            #read() #一次性读完内容
                #如果数据过大容易内存溢出
            #readine()  #一行一行的读
                #不知道在哪结束
                #有的文件是不换行的 例如视频/图片文件 bytes类型没有行的概念 按字节来读
            #readliens()    #一次性读 会默认做分行处理
            #for循环--------------最好 每循环一次就读取一行的数据
        #写
            #write()    #写入 如果需要写多行使用换行符 \n即可
        #光标-------文件指针
            #seek()     指定光标移到到某个位置
            #tell()     获取光标当前的位置
            #truncate() 截取文件
    #关闭文件
        #close

#修改文件
    #文件是直接不能修改的
    #只能读一个 写一个新的 删出一个旧的 将新的重命名为旧的

#python 通过 电脑系统 读取文件 所以open打开文件 编码格式默认为gbk
#当没有写打开方式时默认为r读
with open("Test",encoding='utf-8') as file,open("Test1",'w',encoding='utf-8') as file1:
    for line in file:
        if  '星儿' in line:
            line=line.replace('星儿','阿娇')
        #写文件
        file1.write(line)

import os
os.remove('Test')   #删除文件
os.rename('Test1','测试') #重命名文件

