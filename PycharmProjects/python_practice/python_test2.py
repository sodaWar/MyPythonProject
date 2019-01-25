# -*- coding: UTF-8 -*-
import socket
import itertools
import copy
from datetime import datetime
from collections import deque                                           # collections是python内建的一个集合模块,提供了许多有用的集合类,deque是为了高效实现插入删除操作的双向列表
from collections import defaultdict                                     # 引用key不存在时返回默认值,其他行为跟dict一样
from collections import OrderedDict                                     # 保持dict的key是有序的
from collections import Counter                                         # 统计字符出现个数
import django


# a = [1,2,3,4,['a','b']]                                                 # 原始对象
# b = a                                                                   # 赋值,传对象的引用,对象怎么变它就怎么变
# c = copy.copy(a)                                                        # 对象拷贝,浅拷贝
# d = copy.deepcopy(a)                                                    # 深拷贝
#
# a.append(5)                                                             # 修改对象a
# a[4].append('c')
# print(a)
# print(b)
# print(c)
# print(d)

# a = ['hello',[1,2,3]]
# b = copy.copy(a)
# print([id(x) for x in a])
# print([id(x) for x in b])


# TCP客户端编程
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# s.connect(('127.0.0.1',9999))
# #接收欢迎消息
# mes = s.recv(1024)
# print(mes.decode('utf-8'))
# while 1:
#     cmd = raw_input('please input cmd:')
#     s.sendall(cmd)
#     data = s.recv(1024)
#     print(data)

#UDP客户端编程,面向无连接的协议所以只需要服务器的IP地址和端口号,就可以直接发数据包,所以这里使用sendto函数,比send函数多一个to的参数,且这里不需要建立连接所以没有connect函数
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# for data in [b'Mike',b'apple',b'peach']:
#     #发送数据
#     s.sendto(data,('127.0.0.1',9999))
#     #接收数据
#     print(s.recv(1024).decode('utf-8'))
# s.close()


# deque是为了高效的实现插入和删除操作的双向列表,适用于队列和栈.使用list存储数据时,按索引访问元素很快,但是插入和删除元素就很慢了,因为list是线性存储,数据量大的时候插入和删除效率就会很低
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')                                                      # deque除了实现list的append和pop函数外,还支持appendleft()和popleft()函数
# print(q)

# defaultdict()会在引用的key不存在时,返回一个默认值,该默认值是调用函数时返回的,而dict会抛出KeyError错误.
# d = defaultdict(lambda :'N/A')
# d['key1'] = 'abc'
# print(d['key1'])
# print(d['key2'])



# 使用dict时key是无序的,在对dict做迭代时无法确定key的顺序,而OrdereDict可以保持key的顺序,它是按照key插入的顺序排列,而不是key的本身排序
# d = dict([('a',1),('b',2),('c',3)])
# print(d)
# od = OrderedDict([('a',1),('b',2),('c',3)])
# print(od)

# Counter可以统计字符出现的个数,Counter实际上是dict的一个子类,两个counter可以相加减,相同的key的value相加减
# c = Counter()
# d = Counter(a=3,b=1,c=5)
# for ch in 'programing':
#     c[ch] = c[ch]+1                                                     # 注意该用法,这里注意左边的c[ch]相当于dict的key,右边的c[ch]相当于value,Counter()相当于一个dict,这里意思还需要再深入思考一下？
#     print(ch)
#     print(c)
# print(c)
# print(d)

# dt = datetime(2018,10,19,13,32)
# print(dt)
# print(dt.timestamp)
#
# t = 1429417200.0
# print(datetime.fromtimestamp(t))                                        # timestamp转换为datetime类型,该转换是在timestamp和本地时间做转换



# itertools提供了用于操作迭代对象的函数,count()会创建一个无限的迭代器,会一直重复循环
# x = itertools.count(1)
# for n in x:
#     print(n)

# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限循环下去,如果提供了第二个参数就可以限定重复次数
# ns = itertools.repeat('A',3)
# for i in ns:
#     print(i)

# itertools虽然可以无限迭代,但通常会通过taskwhile()等函数根据条件判断来截取出一个有限的序列
# na = itertools.count(1)
# ns = itertools.takewhile(lambda x : x <= 10,na)                             # 这里lambda函数中na的使用再思考一下？
# print(list(ns))

# chain()可以把一组迭代对象串联起来,形成一个更大的迭代器
# for c in itertools.chain('ABC','XYZ'):
#     print(c)













