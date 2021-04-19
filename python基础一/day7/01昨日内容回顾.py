

#小数据池
'''
int -5~26
str 特殊字符，*数字20

ascii:  8位 1字节 表示1个字符
unicode:    32位 4个字节    表示一个字符
utf-8   1个英文    8位  1个字节
        欧洲  16位 两个字节    表示一个字符
        亚洲  24位 三个字节    表示一个字符

gbk     1个英文    8位  1个字节
        亚洲      16位 两个字节    表示一个字符

'''


s="alex"
b=s.encode('utf-8')
print(type(b))        # b'alex' <class 'bytes'>


#1.基础数据类型汇总补充
'''
str
int
list
    在循环列表时，最好不要删除列表中的元素，会导致列表的索引发生变化，从而发生报错
bool
dict
    1，fromkeys 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值(默认为None 可设置value值)。
tupel

2.集合set
3.深浅copy   
'''
