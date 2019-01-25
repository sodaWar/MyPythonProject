# -* encoding:utf-8 *-
import re                                                               # 正则表达式的包
from datetime import datetime                                           # 提供了操作日期和时间的功能模块
import time                                                             # 处理时间的标准库
import os                                                               # 系统编程的操作模块，用于操作系统的包
import glob                                                             # 用于查找符合特定规则的文件路径名，文件名操作的模块
import subprocess                                                       # 用于创建新进程，管理子进程的包
import threading                                                        # 提供了一个比thread模块更高层的API来提供线程的并发性
import multiprocessing                                                  # 多进程管理包，应该优先考虑使用该包中的函数管理进程，效率更高
import wget                                                             # 一个从网络上自动下载文件的自由工具,所谓自动下载就是可以在用户退出系统之后在后台执行下载,浏览器下载
import math                                                             # 提供函数完成特殊的数学运算
import random                                                           # 用于生成随机数
import sys                                                              # 标准库中自带的一个模块
import calendar                                                         # 日期模块,提供对日期的一些操作方法
import socket                                                           # 提供网络编程一些方法的模块
import pickle                                                           # 将变量序列化的模块
import psutil                                                           # 获得系统信息的第三方模块
import chardet                                                          # 检测对象编码的模块
from PIL import Image,ImageFilter,ImageDraw,ImageFont                   # 图像处理标准库
from timeit import Timer                                                # 计时工具模块,可以计算一段代码运行的时间
from itertools import *                                                 # 迭代器模块,用于创建自定义的迭代器,更加灵活的生成循环器的工具
from io import StringIO                                                 # 在内存中读写str的库
from io import BytesIO                                                  # 在内存中读写bytes的库


# 获取操作系统信息
# print(psutil.cpu_count())                                               # CPU逻辑数量
# print(psutil.cpu_count(logical=False))                                  # CPU物理核心,2是双核超线程,4是4核非超线程
# print(psutil.cpu_times())



# 返回的结果中confidence字段是概率的意思,该函数主要是检测编码的作用
# print(chardet.detect(b'Hello World!'))
# data = '学而时习之'
# print(chardet.detect(data))


# 使用PIL库操作图像缩放
# im = Image.open('month.jpg')                                                    # 打开一个jpg图像文件,这里是当前路径,也可以使用绝对路径
# w,h = im.size                                                                   # 获得图像尺寸
# print("this picture's height and width is %s,%s"%(w,h))
# im.thumbnail((w//2,h//2))                                                        # 将图像尺寸缩放一半,这里注意缩放尺寸的函数返回的对象,没有save()方法,但是下面的函数有
# im3 = im.filter(ImageFilter.BLUR)                                                # 将图像应用模糊滤镜
# im.save('month_zoom.jpg','jpeg')                                                 # 将缩放后的图片用jpeg格式保存
# im3.save('month_blur.jpg','jpeg')


# 生成字母验证码图片
# 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
# # 图像的长和宽240 x 60:
# width = 60 * 4
# height = 60
# # image.new(mode,size.color)使用给定的变量mode和size生成新的图,以及以给定的color填充图像,这里255的意思是一种颜色的所有可能性,rgb是red,green,blue的意思,它们的取值是[0,255]之间的整数.
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象,这个函数从指定的文件加载了一个字体对象,并且为指定大小的字体创建了字体对象:
# font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# # 创建Draw对象,可以对图像对象进行简单的2D绘制:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字,text函数作用是在图像内添加文字,第一个参数是左上角的文本,第二个是要绘制的文本,第三个是字体,第四个是填充文本的颜色:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')




# 序列化一个dict变量,使用dump()方法
# d = dict(name='Apple',age=20,sex='man')
# f = open('test_pickle_dump.txt','wb')
# pickle.dump(d,f)
# f.close()
# 反序列化出对象
# f = open('test_pickle_dump.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)


# 序列化一个dict变量,使用dumps()方法
# d = dict(name='Apple',age=20,sex='man')
# a = pickle.dumps(d)
# f = open('test_pickle_dumps.txt','wb')
# f.write(a)
# f.close()


#查看操作系统的环境变量
# print(os.environ)
# print(os.environ.get('REDIS_HOME'))

# print(os.path.abspath('.'))                                              # 查看当前目录的绝对路径
# a = os.path.join('D:\MyProgram\PythonProject\PycharmProjects\python_practice','test.py')                                # 合并两个路径
# c = os.path.split(a)                                                                                                    # 拆分路径
# b = os.path.splitext(a)                                                                                                 # 拆分路径得到文件扩展名
# print(b)
# os.mkdir('D:/MyProgram/PythonProject/PycharmProjects/python_practice/test.py')
#
# print(os.path.isdir('test'))                                                                                            # 判断当前目录下的test文件的路径是否为目录,该test是相对路径,默认加上当前路径
# print(os.path.isfile('D:/MyProgram/PythonProject/PycharmProjects/python_practice/test.py'))                             # 判断绝对路径test.py文件的路径是否为文件
# print(os.listdir('.'))                                                                                                  # 列出当前目录下的所有目录与文件
# #注意该写法,方便简洁,记下来以后多用！
# print([x for x in os.listdir('.') if os.path.isdir(x)])                                                                 # 列出当前目录下的所有目录,不包括文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])                              # 列出所有.py文件

#写入StringIO的操作
# f = StringIO()
# f.write('hello'.decode('utf-8'))
# f.write(' '.decode('utf-8'))
# f.write('world'.decode('utf-8'))
# print(f.getvalue())


#读取StringIO的操作
# f = StringIO('Hello!\nHi!\nGoodBye!'.decode('utf-8'))
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


#写入BytesIO的操作
# f = BytesIO()
# f.write('ABC'.encode('utf-8'))
# print(f.getvalue())


#TCP客户端编程,创建一个socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# s.connect(('www.sina.com.cn',80))
# #发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# #接收数据
# buffer = []
# while True:
#     #每次最多接收1K字节
#     d = s.recv(1024)
#     #python语言指定任何非0或非null值为true,0或null为false
#     if d:
#         buffer.append(d)
#     else:
#         break
# print(buffer)                                                           #buffer是所有该网站返回的数据字符串列表
# data = b''.join(buffer)                                                 #b''是一个空字节,join是连接列表的函数
# # print(data)                                                             #data就是使用空字节把buffer这个字节列表连接在一起后生成的新字符串
# s.close()
# header,html = data.split(b'\r\n\r\n',1)                                 #注意这里split()效果和''.join()出来的效果是一样的,\r\n\r\n相当于空字节
# print(header.decode('utf-8'))
# #把接收的数据写入文件
# with open('sina.html','wb') as f:
#     f.write(html)


#TCP服务器端编程
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',9999))                                               #创建一个socket后绑定监听的端口和地址
# s.listen(5)                                                              #监听端口,传入的参数表示指定等待连接的最大数量
# print('Waiting for connection....')
#
# def tcplink(sock,addr):
#     print('Accept new connection from %s %s' % addr)
#     sock.send(b'Welcome')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello,%s'%data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('connection from %s:%s closed' % addr)
#
# while True:
#     # 接受一个新连接
#     sock, addr = s.accept()
#     print(sock,addr)
#     # 创建新的线程来处理TCP连接
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()


#UDP服务器端编程,这里不需要监听端口,而是直接接收来自任何客户端的数据
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',9999))
# print('Bind up on 9999 success....')
# while True:
#     # 接收数据
#     data,addr = s.recvfrom(1024)                                            #recvform函数返回数据和客户端的IP地址及端口号,这样就可以再次将数据返回数据给客户端
#     print('Received from %s:%s' %addr,addr)
#     s.sendto(b'Hello,%s!' %data,addr)




#如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句，finally语句是无论程序是否发生异常都会执行的代码
# os.system("chmod -w fool.txt")                                        #去掉文件写入的权限
# os.system("chmod 777 fool.txt")                                       #设置文件所有者访问权限
# try:
#     fo = open("fool.txt","w")
#     fo.write("hi,this is test file")
# except IOError:
#     print "写入权限不足"
# else:
#     print "内容写入成功"
#     fo.close()


# os.rename("foolTest.txt","fool.txt")                                    #将foolTest.txt文件重命名为fool.txt
# os.remove("foolTest.txt")                                               #删除一个已经存在的文件foolTest.txt
# os.mkdir("test")                                                        #该方法有两个参数，路径和创建的目录名，路径默认值为当前目录下
# os.chdir("/Users")                                                      #改变当前的目录，方法中的参数是想设成当前目录的目录名称
# print os.getcwd()                                                       #该方法是显示当前的工作目录
# os.rmdir("test")                                                        #删除目录

#文件在write内容后，直接read文件输出会为空，是因为指针已经在内容末尾。两种解决方式: 其一，先 close 文件，open 后再读取，其二，可以设置指针回到文件最初后再read
# fo = open("fool.txt","wb")
# fo.write("www.runoob.com!\nVery good site!\n")
# fo = open("fool.txt","r+")
# fo.truncate(5)                                                           #截断文件，指定了参数则表示截断文件为size个字符，截断之后后面所有字符会被删除
# str = fo.read()
# print str

# str = fo.read(10)                                                       #read方法中传入的参数是从已打开的文件中的开头开始读入，读取的字节计数
# print str
# fo.close()
# a = fo.tell()                                                           #该方法是显示下一次的读写会发生在文件开头这么多字节之后的数据，即read方法中的参数
# print a
# fo.seek(1,0)                                                            #将读写操作的指针重新定位到文件开头,第二个参数为0,1或2，0是从文件开头开始作为移动字节的参考位置
# b = fo.read(10)                                                         #1是从当前位置，2是从文件末尾开始.第一个参数是要移动的字节数，表示指定开始移动字节的参考位置
# print b

# str = raw_input("please input:")                                        #该函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
# print "you input number is :",str
# str = input("please input:")                                            #该函数与raw_input函数基本类似，但是该函数可以结构一个python表达式作为输入，并将运算结果返回，且不能接受字符串的输入
# print "you input number is :",str

# a = set('adb shell')                                                    #set方法是创建一个集合的方法，且集合中的元素不能重复，如该处只会有一个'l'符号，与列表和元组不同，集合是无序的，无法通过数字进行索引搜索
# print a
# b = set('abcd oplk')
# print a.issubset(b)                                                     #该方法测试如果a中没有任何项在b中，返回True，否则返回False
# print a & b                                                             #集合操作符-两个集合的交集
# print a | b                                                             #并集
# print a == b

# print dir(math)                                                         #该方法用于查询一个模块中定义的所有模块、变量和函数，返回值值是一个列表
# print sys.platform                                                      #sys.platform是得到运行的操作系统环境的命令

# cal = calendar.month(2016,1)                                            #该方法返回值是某年某月的月历，第一个参数是年，第二个参数是月
# print cal
# a = calendar.isleap(2018)                                               #该方法判断一个年数是否为闰年，是闰年则返回True
# print a
# a = calendar.weekday(2018,1,9)
# print a                                                                 #返回给定日期的日期码，返回的值是0-6，对应星期一到星期日

#该函数为不定长参数的函数，该函数能够处理比当初声明时更多的参数
# def printinfo(arg1, *vartuple):                                         #加了星号的变量名会存放所有未命名的变量参数
#     print "输出: "
#     print arg1
#     for var in vartuple:
#         print var
#     return
# printinfo(10)
# printinfo(70, 60, 50)

# globvar = 0
# def set_globvar():                                                      #全局变量想作用于函数内，需要加global
#     global globvar                                                      #global在函数内定义变量相当于定义了一个全局变量，然后改全局变量globvar覆盖了之前定义的globvar变量
#     globvar = 1
#     print globvar                                                       #所以表现为在函数内部改变了变量值
# set_globvar()                                                           #global可同时定义多个变量global x,y,z
# print globvar

#数列翻转函数一
# def reverse(li):
#     a = []
#     for i in range(0, len(li)):
#         a.append(li[-i-1])                                                 #数列从倒序访问的下表是从-1开始，顺序访问从0开始
#     return a
# l = [1, 2, 3, 4, 5]
# b = reverse(l)
# print(b)

#数列翻转函数二
# def reverse(li):
#     for i in range(0, len(li)/2):
#         temp = li[i]
#         li[i] = li[-i-1]                                                    #该函数具体思路待研究
#         li[-i-1] = temp
# l = [1, 2, 3, 4, 5,6]
# reverse(l)
# print(l)

#注意该函数定义的情况！funy不能写成funy()，否则return funy()返回的是funy的函数返回值，所以报错
# def funx(x):
#     def funy(y):
#         return x * y
#     return funy                                                               #return funy返回的是一个对象，可理解为funx是funy的一个对象
# print funx(7)(8)

# a = time.time()
# b = time.gmtime(a)                                                          #返回的时间是格林威治时间，比北京时间少8小时，返回值类型也是时间元组，tm_isdst始终为0
# print b
# c = time.localtime(a)                                                       #返回的时间是当地时间下的时间元组，tm_isdst可取0或1，冬令时是0，夏令时是1
# print c
# def procedure():
#     time.sleep(2.5)
#
# # measure process time
# t0 = time.clock()
# procedure()
# print time.clock() - t0, "seconds process time"
#
# # measure wall time
# t0 = time.time()
# procedure()
# print time.time() - t0, "seconds wall time"



# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict1 = {'Sex' : 'man'}
# print dict.has_key('name')                                             #判断字典中是否存在name这个键，返回True或False
# print dict.items()                                                     #以列表形式返回可遍历的元组数组，包括键和值
# print dict.keys()                                                      #以列表的形式返回字典中所有的键
# dict.update(dict1)                                                     #把字典dict1的键/值对更新到dict里，该方法没有任何返回值，所以该更新方法是更新原来的字典
# a = dict.pop('Name')                                                   #该方法用于删除字典给定键key所对应的值，且返回值为被删除的值，key值必须给出，否则返回default值
# print a
# del dict['Name']                                                       # 删除键是'Name'的条目
# dict.clear()                                                           # 清空词典所有条目
# del dict                                                               # 删除词典，即dict该词典不存在与内存当中了


# localtime = time.localtime(time.time())                                #该方法获得的返回值类型是时间元组类型，注意该类型的数据结构格式
# print localtime
# print localtime.tm_year                                                #可以通过时间元组中的属性名来获得相应的值
# print localtime[0]                                                     #可以通过小标值获得相应的值
# localtime = time.asctime(time.localtime(time.time()))                  #获取可读的时间模式的函数asctime()
# print localtime
# localtime = time.localtime()
# time.strftime("%Y-%m-%d %H:%M:%S",localtime)                           #将一个时间元组的格式数据转换成格式字符串，也就是指定格式的时间，且为string类型的数据
# a = "Sat Mar 09 15:32:15 2018"
# b = time.strptime(a,"%a %b %d %H:%M:%S %Y")
# print b                                                                #将格式字符串转换成一个时间元组的数据
# print time.mktime(b)                                                     #将一个时间元组格式的数据转化成时间戳

# help(time.strftime)                                                    #查一个包中的某个方法的描述，方法不用括号，直接写包名.方法名

# list = [1,2,3,11,21,3]
# print list[1:5]                                                        #截取列表
# print list[-2]                                                         #读取倒数第二个元素
# print max(list)                                                        #返回列表元素中最大值
# print list.index(111)                                                  #从列表中找出某个值第一个匹配项的索引位置，该方法与find()方法差不多，唯一的区别是该方法如果未找到值会抛异常ValueError错误
# print list.pop(2)                                                      #移除列表中的一个元素，如果方法中没有指定索引值，默认为最后一个元素，该方法的参数是索引值，所以知道需要删除的元素索引值，用该方法最合适
# print list.remove(1)                                                   #移除列表中某个值的第一个匹配项，与pop方法的区别在于需要知道移除元素的元素值，而不是索引值，如果该元素值不存在与列表中，会报VauleError错误
# print list.insert(3,'asc')                                             #insert()函数用于将指定对象插入到列表的指定位置中，这里注意插入的可以是对象！该函数没有返回值
# print list                                                             #注意pop()函数与remove函数还有个区别就是，pop函数有返回值，所以print list.pop(2)会显示返回的所移除的元素，而remove函数无返回值，print list.remove(3)显示为None
#
# hi = '   aAsdASDK   '
# a = hi.swapcase()                                                     #swapcase()方法是翻转字符串中的大小写，即大写变小写，小写变大写
# a = hi.isdigit()                                                      #该方法是判断如果string只包含数字则返回True，否则返回False
# a = hi.lower()                                                        #将string中大写字母转换为小写字母
# a = max(hi)                                                           #返回字符串中最大的字母
# a = hi.replace('A','a')                                               #string.replace(str1, str2,  num=string.count(str1))方法
# a = hi.strip()                                                        #该方法是去除字符串首尾的空格
# print a                                                                 #replace()方法是把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次
#
# print type(math.modf(100))                                            #modf(x)方法返回x的整数与小数部分，且都是浮点型数据，返回值以元组形式返回
# x = 7
# print eval('3*7')                                                     #eval()方法用来执行一个字符串表达式，并返回表达式的值
# print eval('pow(2,2)')
#
# def height_class(h):
#     if h > 180:
#         return "tall"
#     elif h < 160:
#         return "short"
#     else:
#         return "middle"
#
# friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
# friends.sort()                                                           #sort()函数没有返回值，但是会对列表的对象进行排序，且是对原列表进行排序
# print friends
# friends = sorted(friends, key = height_class)                            #sorted()函数是一个内置函数，返回重新排序的列表，注意返回的结果是一个新的list，而不是之前的列表
# for m, n in groupby(friends, key = height_class):
#     print(m)
#     print(list(n))
#
#
# res = imap(pow, [1, 2, 3], [1, 2, 3])                                   #pow()是内置的乘方函数，如pow(3)就是3的3次方
# for num in res:                                                         #imap()返回的结果是循环器
#     print(num)
#
# def lowToBig(s):
#   return s.upper()                                                        #因此map()函数能够用于多个参数使用同一个函数的情况下
# print map(lowToBig,'asdfd')                                               #map(function, sequence) ：对sequence中的item依次执行function(item)，结果返回以列表形式
#
# def demo1(value):
#     result = []
#     while value:                                                         #按从最低位（个位）到最高位的顺序获取每位数字
#         result.append(value % 10)                                        #单引号返回除法的值，但要注意如果要得到小数部分，其中必须有一个除数的值是float类型.而%是取余数
#         value = value // 10                                              #双斜杠是取整除,返回商的整数部分，如9//2输出结果是4
#     result.reverse()                                                     #逆序，按正常的顺序返回
#     return result
#
# def demo2(value):
#     result = []
#     while value:                                                        #divmod()是内置函数，返回整商和余数组成的元组
#         value, r = divmod(value, 10)                                    #divmod(a,b)方法返回的是a//b（商）以及a%b(余数)，返回结果类型为tuple
#         result.append(r)                                                #该方法将demo1的方法中取商和取余数两个步骤合为一步，所以运行速度更快一点
#     result.reverse()
#     return result
#
# def demo3(value):
#     # print map(int,str(value))
#     return map(int, str(value))                                         #字符串是Python不可变序列的一种,map()函数可以实现将其他类型的数据转换成list，但是这种类型的数据
#                                                                         #只能是不可变的数据类型，如元组，字符串等.list()函数是将元组转换为列表
# def main():
#     value = random.randint(1, 100000000)
#     print(value)
#
#     #测试次数
#     times = 10000000
#
#     #分别测试3种方法的运行时间
#     print(Timer(repr(demo1(value)), 'from __main__ import demo1').timeit(times))        #str()和repr()方法可以将任意值转换为字符串，但是str()方法转换的值是给人看的字符串
#
#     print(Timer(repr(demo2(value)), 'from __main__ import demo2').timeit(times))        #repr()方法转换的值是给机器看的字符串.事实上，str的内置函数__str__只是覆盖了repr的内置函数__repr__
#
#     print(Timer(repr(demo3(value)), 'from __main__ import demo3').timeit(times))        #__repr__是更底层的函数，面向程序员，而__str__面向用户
#
# main()                                                                                  #注意Timer()方法的使用
#
# a = int(random.randint(9999999,100000000))                              #生成一个范围内的随机整数
# print a
#
# help(wget)                                                            #查看一个包、库中或者具体某个函数如wget.download()的api说明
#
# def f(url):
#     wget.download(url)                                                  #下载网站的首页到一个文件中，默认为download.wget文件
# pool = multiprocessing.Pool(3)                                          #创建了包含3个进程的进程池
# rel  = pool.map(f,['https://www.baidu.com/','https://www.douban.com/','https://www.sina.com/'])
# print(rel)
# pool.close()                                        #如果不用进程池的话，需要通过循环创建多个子进程，然后添加到列表中，最后循环子进程的列表，调用进程的join函数.
# pool.join()                                         #主线程会在join的地方一直等子进程结束，不然子进程不会并发运行，所以建议使用进程池
#
# def f(n, a):
#     n.value   = 3.14
#     a[0]      = 5
#
# num   = multiprocessing.Value('d', 0.0)                                 #在主进程中创建Value和Array两个对象，为共享的内存
# arr   = multiprocessing.Array('i', range(10))
#
# p = multiprocessing.Process(target=f, args=(num, arr))                  #Process对象的子进程，该进程中修改了Value和Array对象的值，在之后回到主进程后打印出结果
# p.start()
# p.join()
# print num.value                                                         #该两个对象的值发生了变化，说明资源可以在两个进程之间共享
# print arr[:]
#
# # worker function
# def worker(sign, lock):
#     lock.acquire()
#     print(sign, os.getpid())
#     lock.release()
#
# Main
# print('Main:',os.getpid())
#
# # Multi-thread
# record = []
# lock  = threading.Lock()
# for i in range(5):
#     thread = threading.Thread(target=worker,args=('thread',lock))
#     thread.start()
#     record.append(thread)                                                 #所有线程的pid都和主进程的pid相同
#
# for thread in record:
#     thread.join()
#
# Multi-process
# record = []
# lock = multiprocessing.Lock()                                              #不同进程的pid是不相同的，使用lock同步是因为所有任务在打印时都会向一个标准输出stdout输出
# for n in range(5):                                                          #这样字符就会混在一起无法阅读，所以用lock同步可以避免多个任务同时向终端输出
#     process = multiprocessing.Process(target=worker,args=('process',lock))
#     process.start()                                                         #启动进程
#     record.append(process)                                                  #添加进程到进程列表中
#
# for process in record:
#     process.join()                                                          #等待所有进程完成
#
# out = subprocess.call("ls -l", shell=True)
# out = subprocess.call("cd ..", shell=True)
#
# path = '/Users/apple/auto_test/python_test.py/..'
# path1 = '/Users/apple/auto_test/*'
# print (glob.glob(path1))                                            # 查询目录下文件的方法
# print(os.path.basename(path))                                       # 查询路径中包含的文件名
# print(os.path.dirname(path))                                        # 查询路径中包含的目录
# info = os.path.split(path)                                            # 将路径分割成文件名和目录两个部分，放在一个表中返回
# print os.path.normpath(path)                                          # 去除路径path中的冗余。比如'/home/vamei/../.'被转化为'/home'
# print info
# path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')        # 使用目录名和文件名构成一个路径字符串，注意该构成字符串的方式！！路径字符串和日期格式的字符串更多使用该方式
# print path2
# p_list = [path, path2]
# print p_list
# print(os.path.commonprefix(p_list))                                    # 查询多个路径的共同部分，将多个路径放在一个列表中，然后使用os.path.commonprefix()方法查询
#
# t      = datetime.datetime(2012,9,3,21,30)
# t_next = datetime.datetime(2012,9,5,23,30)
# delta1 = datetime.timedelta(seconds = 600)                        #datetime包中定义了时间间隔对象timedelta，一个时间加上一个时间间隔可以得到一个新的时间点
# delta2 = datetime.timedelta(weeks = 3)                            #两个时间点相减会得到一个时间间隔
# print(t + delta1)
# print(t + delta2)
# print(t_next - t)
#
# t = datetime.datetime(2012,9,3,21,30)                                   #将指定的时间转换成datetime格式的日期,很有用
# print(t)
# st = time.gmtime()      # 返回struct_time格式的UTC时间
# st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
# s  = time.mktime(st)
# print s
# m = re.search('[0-9]','abc2d4ef')
# a = re.findall('[0-9]','asds24da29ad')
# print(type(m.group(0)))
# m = re.search("\d{4}\.\d{2}\.\d{2}", "output_1981.10.21.txt")
# a = re.sub('[\.]','',m.group(0))                            #将字符串中的点号用空来替换，并返回新的字符串
# week = datetime.strptime(a,'%Y%m%d')                        #将字符串转换为指定格式的日期时间
# print week
# print week.day
# print week.weekday()                                        #查看该日期是周几的方法
# b = str(week.year) + '-' + str(week.month) + '-' + str(week.day) + '-' + str(week.weekday() + 1)
# c = 'output_' + b + '.txt'
# print c
#
# a = 'python_test.txt'
# with open(a,"w") as f:
#     f.write('tom,12,86\r')
#     f.write('Lee,15,99\r')
#     f.write('Lucy,11,58\r')
#     f.write('Jesy,19,56')
# with open(a,'r') as k:
#     b = k.readlines()
#     c = b[0].split('\r')
#     x = 0
#     for i in range(len(c)):
#         d = c[i].split(',')                                     #返回True或False
#         if int(d[2]) < 60:
#             print d[0] + ',' + d[2]                              # 得分低于60分的人姓名
#         if 'L' in d[0]:
#             print d[0]
#         if d[0].find('L') != -1:                              #返回所查找的字符串索引，查找姓名以L开头的人
#             print d[0]
#         print int(d[2])
#         x = x + int(d[2])                                     #所有人总分
#         print x
#         if d[0][0].isupper() == False:
#             a = d[0][0].upper()
#             print a
#             print d[0]
#             d[0] = a + d[0][1:]                                     #该字符串首字母如果是小写，就改成大写
#             print d[0]
#
# li = [1, 2, 3, 4, 5, 6]
# print(li[3])
# print(li.__getitem__(2))                                        #上面的程序运行到li[3]的时候，Python发现并理解[]符号，然后调用__getitem__()方法
# li.__setitem__(4,10)                                            #与运算符类似，许多内置函数都是调用对象的特殊方法来实现函数的功能
# print li
# c = {'a' : 1,'b':2}
# c.__delitem__('a')
# print c
#
# class num(object):
#     def __init__(self, value):
#         self.value = value
#     def getNeg(self):
#         return -self.value
#     def setNeg(self, value):
#         self.value = -value
#     def delNeg(self):
#         print("value also deleted")
#         del self.value
#     neg = property(getNeg, setNeg, delNeg, "I'm negative")
#
# x = num(1.1)
# print(x.neg)                                                      #闭包
# x.neg = -22
# print(x.value)
# print(num.neg.__doc__)
# del x.neg
#
#
#
# a new wrapper layer
# def pre_str(pre=''):
#     # old decorator
#     def decorator(F):                                             #装饰器，之后与闭包一起待研究深透
#         def new_F(a, b):
#             print(pre + "input", a, b)
#             return F(a, b)
#         return new_F
#     return decorator
#
# # get square sum
# @pre_str('^_^')
# def square_sum(a, b):
#     return a**2 + b**2
#
# # get square diff
# @pre_str('T_T')
# def square_diff(a, b):
#     return a**2 - b**2
#
# print(square_sum(3, 4))
# print(square_diff(3, 4))
#
# a = [1,2,3]
# del a[0]                                                              #删除列表中某个元素
# print(a)
# input('please:')                                                      #用户在控制台输入信息
# print("I'm %s. I'm %d year old" % ('Vamei', 99))                      #字符串格式化，%操作符的使用
# print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})                          #使用词典来传递真实值的方式
