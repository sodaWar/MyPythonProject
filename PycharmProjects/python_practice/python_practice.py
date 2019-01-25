# -*- coding: UTF-8 -*-
from math import sqrt
from sys import stdout
from collections import deque
from Tkinter import *
import time
import math
import datetime
import numpy as np
import random
import turtle

# for data in [b'Mike',b'Bird',b'Panda']:
#     发送数据
    # s.send(data)
    # print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()



# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# b = []
# for i in range(1,5):
#     for m in range(1,5):
#         for n in range(1,5):
#             if (i != m) and (i != n) and (m != n):                                          #判断3个循环中数字互相不等即可
#                 a = i * 100 + m * 10 + n * 1
#                 b.append(a)
#                 print a
# print len(b)

# 从键盘输入当月利润I，求应发放奖金总数,方法一,最笨的方法
# a = input("please input the mouth profit ：")
# if a < 100000 or a == 100000:
#     b = a * 0.1
#     print b
# elif 100001 < a <= 200000:
#     b = 10000 + (a - 100000) * 0.075
#     print b
# elif 200001 < a <= 400000:
#     b = 10000 + 7500 + (a - 200000) * 0.05
#     print b
# elif 400001 < a <= 600000:
#     b = 10000 + 7500 + 10000 + (a - 400000) * 0.03
#     print b
# elif 600001 < a <= 1000000:
#     b = 10000 + 7500 + 10000 + 6000 + (a - 600000) * 0.015
#     print b
# elif a > 1000000:
#     b = 10000 + 7500 + 10000 + 6000 + 6000 + (a - 1000000) * 0.01
#     print b
# else:
#     print '输入有误，请重新输入'

# 方法二，使用字典控制利润与提成比例的匹配：
# num = int(raw_input("请输入今年的公司利润："))
# obj = {100: 0.01, 60: 0.015, 40: 0.03, 20: 0.05, 10: 0.075, 0: 0.1}                      #这个0也有提成比例率是有原因的
# keys = obj.keys()
# keys.sort()                                                                              #对原列表进行排序
# keys.reverse()                                                                           #对原列表进行倒序排列，这里倒序排列是有道理的，用于与用户输入的利润值比较时应该从大到小比较
# r = 0
# for key in keys:
#     if num > key:                                                                        #如输入的是65万，将65-60万乘以相应的提成率
#         r += (num - key) * obj.get(key)                                                  #该方法很好，以后应该尝试用该方法来处理一些逻辑
#         num = key                                                                        #然后将num值赋值为60万，一直循环到0即结束
# print "今年的奖金为：", r, "万元."

# 输入某年某月某日，判断这一天是这一年的第几天
# try:
#     num = raw_input("请输入年月日（格式如：2017-04-04）:")
#     a = time.strptime(num,"%Y-%m-%d")                                                     #该函数根据指定的格式把一个时间字符串解析为时间元组
#     print(time.strftime("今年的第%j天",a))                                                 #这个日期格式化符号%j代表年内的一天，可以直接显示出一个日期是一年中的第几天
#     print(time.strftime("今天是星期%w天",a))                                               #这个日期格式化符号%w代表一个时间所对应的星期数，且以星期天为一星期的开始
# except ValueError:
#     print '输入时间有误，请重新输入'

# 判断一个年份是否为闰年
# year = int(raw_input("请输入年份:"))
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     print '是闰年'
# else:
#     print '不是闰年'


# 输入三个整数x,y,z，请把这三个数由小到大输出
# a = int(raw_input("输入第一个数：\n"))
# b = int(raw_input("输入第二个数：\n"))
# c = int(raw_input("输入第三个数：\n"))
# m = [a,b,c]
# m.sort()
# print  m
#
# m = []
# for i in range(3):
#     x = int(raw_input('请输入数字:\n'))
#     m.append(x)
# m.sort()
# print m

# 赋值a数列到b数列中,这里注意c的值和b相同,他们的区别在于,直接=是引用赋值,引用原来的对象;而[:]是重新推导,会生成新的对象,id函数能够得到函数的对象地址,可通过其看出它们的区别
# a = [1,2,3,4]
# b = a[:]
# c = a
# print id(a),id(b),id(c)

# 输出 9*9 乘法口诀表
# for m in range(1,10):
#     for n in range(1,10):
#         if(m >= n):                                                   # 该方式循环会使得else中的数输出过多空行，即m<n的情况也会输出很多空行，所以应该先筛选出符合条件的数字进行循环，如下循环
#             print str(m) + '*' + str(n) + '=' + str(m * n) ,
#         else:
#             print


# for i in range(1, 10):
#     if i == 1:
#         print "%d*%d=%d" % (1, 1, 1 * 1),
#     else:
#         print
#         for j in range(1, i+1):
#             print "%d*%d=%d" % (i, j, i*j),                             # 如果想要在print后不换行,在2.x版本可以在末尾加上逗号即可如print x,这样就行,但在3.x版本中需要写成print(x,end='')

# a = [1, 1]                                                              # 递推数列
# for i in range(24):
#     b = a[-1] + a[-2]
#     a.append(b)
# print a

# 判断一个数字是否为素数，判断方法是循环除以2-自身数字的范围内所有数字，如果有整除，那么该数就不为素数.判断101-200之间有多少个素数
# m = []
# for i in range(101,200):
#     for j in range(2,i):
#         if i % j == 0:                                        # 该方法有个缺点就是需要将101-200之间的数字，除以2-自身数字的范围内所有的数字，这样会降低程序运行效率，增加运行时间
#             break
#     else:
#         m.append(i)
# print m

# m = []
# for i in range(101,201):
#     for j in range(2,int(sqrt(i))+1):                       # 通过sqrt()方法得出一个数的平方根,只需要将一个数字除以2到平方根+1范围内所有的数字，即可判断是否为素数，提高了效率，减少了运行时间
#         if i % j == 0:
#             break
#     else:
#         m.append(i)                                        # 这里注意for/else循环语句，for循环之后还可以有else语句，作用是for循环中if条件一直不满足，则最后就执行else语句
# n=len(m)                                                   # 并且注意当循环是由break语句中断时，else就不会被执行，但是for循环正常退出的话else语句还是会被执行
# print m
# print '总数为：',n

# 打印所有的水仙花数，水仙花数指其各位数字立方和等于该数本身
# m = []
# for i in range(100,1000):
#     a = i // 100                                             #百位数字
#     b = i // 10 % 10                                         #十位数字
#     c = i % 10                                               #个位数字
#     d = a**3 + b**3 + c**3                                   #//和/两种运算符,在进行整数运算时没有差别,在进行浮点数运算时,//取小数点前的值(但该值的类型还是浮点型),/就是带小数点后面的运算了
#     if d == i:
#         m.append(i)
# print m


# 获取一个数字中的各个位置的数字，如个位、十位、百位等
# result = []
# value = 1234
# while value:
#     result.append(value % 10)
#     value = value // 10
# print result

# 输出指定格式的日期
# print datetime.datetime.today()
# print datetime.datetime.today().strftime('%Y-%m-%d')                                      #该方法与time模块中使用方式有略微不同,time模块中该方法内的参数包括时间
# a = datetime.date(2018, 10, 12)                                                             #创建日期对象
# print(a.strftime('%d/%m/%Y'))
# b = a + datetime.timedelta(days=1)                                                          #日期算术运算使用tomedelta方法，该方法不能运算年、月
# print b
# b = a.replace(year=a.year + 1)                                                              #replace()方法的参数为date.replace(year, month, day)，可替换年，月，日
# print b                                                                                     #该方法返回一个新的datetime对象，这个新的对象在其他字段上与原有对象保持一致


# 输入一行字符,分别统计出其中英文字母、空格、数字和其它字符的个数
# def count(s):
#     count_a = count_b = count_c = count_d = 0
#     for i in s:
#         if 97 <= ord(i)<=122 or 65 <= ord(i) <= 90:                                           #ord()函数与chr()函数可以理解为相反作用的函数，ord函数是将一个字符转换为相对应的ASCII数值
#             count_a = count_a + 1                                                             #chr函数是将一个ASCII数值转换为相对应的字符，参数范围在0-256，具体ASCII码所对应的数值表格可在网上查看
#         elif 48 <= ord(i) <= 57:                                                              #大小写字母、数字以及空格、回车、换行符等都有相对应的ASCII码，根据ord()以及对应的ASCII码即可判断不同的字符
#             count_b = count_b +1
#         elif ord(i) == 32:                                                                    #chr(13) 是一个回车，Chr(10) 是个换行符,chr(32)是个空格符
#             count_c = count_c + 1
#         else:
#             count_d = count_d + 1
#     print('中英文字母有' + str(count_a) + '个')
#     print('数字有' + str(count_b) + '个')
#     print('空格有' + str(count_c) + '个')
#     print('其他字符有' + str(count_d) + '个')
# if __name__ == "__main__":
#     s = raw_input("请输入一行字符:")
#     count(s)


# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222+222222+22222+2222+222+22+2(此时共有5个数相加)，几个数相加由键盘控制。方法一：
# def add(a,n):
#     b = []
#     c = []
#     for i in range(n):
#         sn = 10 ** (i) * a
#         b.append(sn)
#     print b
#     for j in range(len(b)):
#         if j == 0:
#             c.append(sum(b))
#         else:
#             b.pop(len(b)-1)
#             c.append(sum(b))
#             print c
#     c.reverse()
#     d = sum(c)
#     print d
#     c.pop(len(c)-1)
#     e =sum(c)
#     print e
#     print d + e
# if __name__ == "__main__":
#     a = int(raw_input("请输入所需要相加操作的数字："))                          #python2.x中.raw_input()函数将所有输入作为字符串看待,返回字符串类型.input()只能接收数字的输入,不能接收字符串输入
#     n = int(raw_input("请输入所需要加的次数："))
#     add(a,n)

# 方法二：
# Tn = 0
# Sn = []
# n = int(raw_input('n = '))
# a = int(raw_input('a = '))
# for count in range(n):
#     Tn = Tn + a
#     a = a * 10                                                                 #只需要在循环中将a的值变化一下就能够继续让新的a值用于下一次循环了，方法一没有该操作因此更麻烦
#     Sn.append(Tn)                                                              #记住该方法，循环体中可以改变所需要循环的值用于下一次循环
#     print Tn
# print Sn
# Sn = reduce(lambda x,y : x + y,Sn)                                             #reduce()方法第一个参数是函数方法，第二个是一个数据集合，将函数先对集合中第1，2个数据进行操作，得到的结果再与第三个数据代入函数进行操作
# print "计算和为：",Sn
#
# # 方法三，简化方法二，该两个方法特别重要，具有很强参考性:
# n = int(input('n = '))
# a = int(input('a = '))
# sum = 0
# total = 0
# for i in range(n):
#     sum += (10 ** i)                                                            #该方法简化方法一，也是在循环内改变了下一次循环所用的数据，并且是两个，所以代码更简单适用
#     total += sum * a
# print(total)

# 方法四，使用拼接数字的方式来处理
# n = int(raw_input("input you number:"))
# c = int(raw_input("input you time:"))
# def num(n,time):                                                                  #拼接数字，如n =3，time = 4返回3333
#     l = []
#     while time > 0:
#         l.append(str(n))
#         time -= 1
#     l = ''.join(l)                                                                # join函数可以将list转换成字符串,该行含义是将通过空白字符来连接序列中的元素,结果返回字符串
#     return int(l)
# sum = 0
# for i in range(1,c + 1):
#     j= num(n,i)
#     sum = sum + j
# print sum


# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第n次落地时，共经过多少米？第n次反弹多高？
# def rebound(n):
#     b =[]
#     for i in range(2,n+2):
#         a = float(100) / (2**(i-1))
#         b.append(a)
#     print "反弹" + str(b[-1])
#     print(b)
#     b.pop(-1)
#     c = 100 + sum(b) * 2
#     print "经过"+str(n)+"次落地后，共经过"+str(c)
# if __name__ == "__main__":
#     n = int(raw_input("请输入落地次数:"))
#     rebound(n)


# n=['a','b','c']
# m=[]
# for i in range(3):
#     if n[i]!='a' and n[i]!='c':
#         m.insert(i,'x')
#     elif n[i]!='c':
#         m.insert(i,'z')
#     else:
#         m.insert(i,'y')
# print(m)
# print 'a--%s, b--%s, c--%s' %(m[0], m[1], m[2])

# 打印出菱形图案
# n = 7
# for i in range(n):
#     a = ' ' * (n-i-1) + '*'*(1 + 2 * i) + ' ' * (n-i-1)
#     print a
# a = 2 * (n-1) -1
# for j in range(n):
#     b = ' '* (j+1) + '*'*(a - 2 * j) + ' '* (j+1)                                                               # a也可以代入表达式a-2*j中直接用n来进行运算
#     print b


# 斐波那契数列的实现如1,1,2,3,5,8,13....

# def fib_loop(n):                                                                                                  #递归方法
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
# for i in range(20):
#     print(fib_loop(i))
#
# Sn = reduce(lambda x,y : x + y,Sn)

# def fib_loop(n):
#     a, b = 2, 3
#     for i in range(n):
#         a, b = b, a + b
#     return a
#
# for i in range(20):
#     print(fib_loop(i))


#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和.该有规律

# a = 1.0
# b = 2.0
# s = 0
# for i in range(1,21):
#     s += b / a
#     t = b
#     b = a + b
#     a = t
# print s

#求1+2!+3!+...+20!的和，方法一

# n = 0
# s = 0                                                                          #从这个方法中看出，一个算法的实现，逻辑很重要，该方法是最简捷的方法，主要因为它的逻辑很正确
# t = 1                                                                          #该方法的算法逻辑是将n! = n * (n-1)!来实现的，这样算就使得方法写出来很简捷了，这种逻辑是将n!与(n-1)!产生联系
# for n in range(1,21):
#     t *= n
#     print t
#     s += t
#     print s
# print '1! + 2! + 3! + ... + 20! = %d' % s

#方法二,使用map函数
# s = 0
# l = range(1,21)
# def op(x):
#     r = 1
#     for i in range(1,x + 1):
#         r *= i
#     return r
# s = sum(map(op,l))                                                               #这里最重要的是使用了map()函数，而且算法实现的逻辑是将每个n!与(n-1)!都单独算出，每个阶乘都是单独的算法无联系
# print '1! + 2! + 3! + ... + 20! = %d' % s

#方法三,通过while方法
# sum1=0
# for each in range(1,21):                                                           #该方法也是将每个阶乘都当成一个单独的个体来进行算术，该处最重要的用了while循环来算出某个阶乘的值
#     sum2=1                                                                         #然后通过循环算出各个阶乘的值，最后相加
#     while each>1:
#         sum2=sum2*each
#         each-=1
#     print sum2
#     sum1+=sum2
# print(sum1)

#方法四，通过嵌套的for循环
# s = 0
# for i in range(1, 21):
#     r = 1
#     for j in range(1, i+1):
#         r *= j
#     s += r
# print(s)


#利用递归方法求5!,递归方法的实现就是在方法中调用自身方法，这样就能实现递归调用方法了

# def recursion(n):
#     s = 0
#     if n == 0:
#         s = 1
#     else:
#         s = n * recursion(n-1)
#     return s
# for i in range(5):
#     print '%d! = %d' % (i,recursion(i))

#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来.
# 方法一将输入的字符串转换成数列形式进行操作，因为字符串不不可修改的变量，因此经过函数操作后实际字符串还是不变，比较难于操作，因此先转换为列表形式
# n = raw_input("请输入5个字符:")
# l = list(n)
# def recursion(l):
#     print l[-1]
#     del l[-1]
# for i in range(5):
#     recursion(l)

#方法二，先转换为list形式，然后通过reverse函数将数列倒序后输出即可，但是该方法不是利用递归方法来实现的
# S = input('Input a string:')
# L = list(S)
# L.reverse()
# for i in range(len(L)):
#     print(L[i])

#方法三,注意下该实现的方式
# def output(s, l):
#     if l == 0:
#         return
#     print (s[l - 1])
#     output(s, l - 1)
#
# s = raw_input('Input a string:')
# l = len(s)
# output(s, l)

#有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
#利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推
#该题主要是这种递归的思维方式，这种算法逻辑的实现很重要

# def age(n):
#     if n == 1:
#         c = 10
#     else:
#         c = age(n - 1) + 2
#     return c
# print age(5)


#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

# n = raw_input("请输入一个不多于5位的正整数:")
# l = list(n)
# print len(l)
# l.reverse()
# for i in range(len(l)):
#     print l[i]

#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同.方法一
# n = raw_input("请输入一个数字:")
# def palindromic(n):
#     l = list(n)
#     if len(l) % 2 == 0:
#         print '该数不是回文数'
#     else:
#         for i in range((len(l)-1)/2):
#             if l[i] == l[-i-1]:
#                 continue
#             else:
#                 return 0
# a = palindromic(n)
# if a == 0:
#     print '该数不是回文数'
# else:
#     print '该数是回文数'

#方法二,用列表反转法,利用回文数的特性，左右对称相等，因此将回文数转换成列表后再倒序应该与之前的列表相等，这种特性来实现更快
# s=input('Pleae enter 5 numbers:>>>')
# li1=[]
# li2=[]
# for i in s:
#     li1.append(i)
#     li2.append(i)
# li2.reverse()
# print(li1,li2)
# if li1== li2:
#     print('Yes')
# else:
#     print('No')

#按逗号分隔列表并显示，方法一

# l = [1,2,3,4,5,6,7]
# o = ''
# for i in l:
#     o += str(i)+','
# print(o[0:-1])

#方法二
# L = [1,2,3,4,5]
# s1 = ','.join(str(n) for n in L)                                                        #这种将列表转换成字符串序列的写法注意!有点不懂待之后解决
# print s1

#方法三,将列表转换成str类型显示出来即可
# L = [1, 2, 3, 4, 5]
# L = str(L)[1:-1]
# print L                                                                                 #repr()是将一个对象转成字符串显示

#文本颜色设置

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print bcolors.OKGREEN + "警告的颜色字体?" + bcolors.ENDC


#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中

# a = [1,3,5,9,12,25,31]
# n = input("请输入一个正整数:")
# for i in range(len(a)):
#     if n < a[i]:
#         a.insert(i,n)
#         print a
#         break

#将一个数组逆序输出,方法一使用reverse()方法
# b =[1,31,12,11,42]
# print b[::-1]                                                                                     #倒序输出的一种方法
# b.reverse()
# print b

#方法二用第一个与最后一个交换,主要是锻炼不同的思维逻辑来思考一个问题
# n = raw_input("请输入一组数列(格式如a,b,c,d):")
# l = n.split(",")                                                                                #这里注意需要将用户输入的字符串进行分割，该方法会以数列的形式返回分割字符串后的值
# if len(l) % 2 == 0:
#     for i in range(len(l)/2):
#         t = l[i]
#         l[i] = l[-i-1]
#         l[-i-1] = t
# print l

#类的属性和方法的属性的区别
# def varfunc():
#     var = 0
#     print 'var = %d' % var
#     var += 1
# if __name__ == '__main__':
#     for i in range(3):
#         varfunc()
#
# # 类的属性
# class Static:
#     StaticVar = 5
#     def varfunc(self):
#         self.StaticVar += 1
#         print self.StaticVar
#
# print Static.StaticVar
# a = Static()
# for i in range(3):
#     a.varfunc()

#两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵.这里要注意创建二维以及以后多维的数组具体定义的方式,python没有直接定义使用的二维数组，一般创建多维数组的方法是使用列表解析方法

# x = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# z = [['' for j in range(1, 4)] for i in range(1, 4)]                                                                #默认值为''即空
# for i in range(3):
#     for j in range(3):
#         z[i][j] = x[i][j] + y[i][j]
# print z

#方法二,使用numpy库,直接将两个数列相加，两个数列对应位置即索引相同的数会相加
# x = np.array( [[12,7,3],
#                [4 ,5,6],
#                [7 ,8,9]])
# y = np.array( [[5,8,1],
#                [6,7,3],
#                [4,5,9]])
#
# z = x+y
# print z

#方法三,使用map函数,该方法是将数列的每行作为一个单独的模块先算出来,注意这里的map函数使用,map函数中seq序列参数多于一个时,map可以并行地执行seq参数。
#当map函数seq序列多于一个时，每个seq的同一位置的元素同时传入一个多元的func函数之后，得到一个返回值，并将这个返回值存放在一个列表中.这个是多个seq参数使用的很好的例子
# x = [[12,7,3],
#     [4,5,6],
#     [7,8,9]]
#
# y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# z = []
# for i in range(3):
#     zz = map(lambda a,b:a+b, x[i],y[i])
#     z.append(zz)
# print z

#求输入数字的平方，如果平方运算后小于 50 则退出.这里重点注意quit()方法用于退出程序作用,以及使用while方法来循环和继续运行程序的作用

# while(1):
#     n = input("请输入一个整数:")
#     print '运算结果为: %d' % (n**2)
#     if n**2 < 50:
#         quit()
#     else:
#         print '请继续输入'

#使用lambda来创建匿名函数,注意下这里获取用户输入的两个值得方法,x,y = input()

# h=lambda x,y:x//y
# x,y=input('请输入两个数字，并以逗号分隔：')
# print(h(x,y))

#输出一个随机数

# print random.random()                                                                                           #输入0-1之间的随机数
# print random.uniform(10,20)                                                                                     #输出10-20之间的随机数
# print random.randint(10,20)                                                                                     #输出10-20之间的随机整数

#画图,方法一使用circle画圆形

# if __name__ == '__main__':
#     canvas = Canvas(width=800, height=600, bg='yellow')
#     canvas.pack(expand=YES, fill=BOTH)
#     k = 1
#     j = 1
#     for i in range(0, 26):
#         canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
#         k += j
#         j += 0.3
#
#     mainloop()

#方法二使用turtle模块画图,该方式更简单,以后涉及该方便需先学习该模块的使用
# if __name__ == '__main__':
#     pen=turtle.Turtle()
#     pen.color("yellow")
#     pen.width(5)
#     pen.shape("turtle")
#     pen.speed(1)
#     pen.circle(100)

#使用circle画直线

# canvas=Canvas(width=300,height=300,bg='white')
# canvas.pack(expand=YES, fill=BOTH)
# x1,y1=50,20
# x2,y2=100,20
# x3,y3=75,40
# x4,y4=75,100
# canvas.create_line(x1,y1,x3,y3, width=3, fill='red')
# canvas.create_line(x2,y2,x3,y3, width=3, fill='red')
# canvas.create_line(x1,y1,x4,y4, width=3, fill='red')
# canvas.create_line(x2,y2,x4,y4, width=3, fill='red')
# mainloop()

#使用turtle模块画直线
# def drawline(n):
#     t=turtle.Pen()
#     t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
#     t.begin_fill()   #开始填充颜色
#     for i in range(n): #任意边形
#         t.forward(50)
#         t.left(360/n)
#     t.end_fill()    #结束填充颜色
# drawline(4)
# time.sleep(10)

#使用rectangle画方形.画图可以使用TKinter和turtle模块,使用时再学习
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Canvas')
#     canvas = Canvas(root, width=400, height=400, bg='yellow')
#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_rectangle(x0, y0, x1, y1)
#         x0 -= 5
#         y0 -= 5
#         x1 += 5
#         y1 += 5
#     canvas.pack()
#     root.mainloop()

#打印出杨辉三角,方法一通过多重循环,并且每次循环后更新a的值作为下一次循环的条件,从而实现了该功能.该题还有诸多算法,可有时间查看！

# n = input("请输入需要打印出多少行的数字:")
# def triangle(n):
#     a = [1]
#     for i in range(n):
#         b = [1, 1]                                                               #这个b列表在这个位置是处于两个for循环之间,主要作用是为了每次打印下一行时b列表都不变为1,1
#         for j in range(len(a)-1):
#             c = a[j] + a[j+1]
#             b.insert(1,c)
#         a = b                                                                    #a列表在这个位置,是为了在第二次循环后,将b值赋给a数列，然后a数列能够用于下一次打印下一行的循环中
#         for m in range(len(b)):
#             if m < len(b) - 1:
#                 print b[m],
#             else:
#                 print b[m]
# print 1
# triangle(n)

#方法二,通过递归方法实现,多思考该方式的实现原理
# n =10
# def lst(i,j):
#     if i==j or j==1:
#         return 1
#     else:
#         return lst(i-1,j-1) + lst(i-1,j)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print lst(i,j),
#     print

#方法三
# a = s = [1]
# for i in range(0,10):
#     for j in range(i+1):
#         if j == 0 or i == j:
#             s.append(1)
#             print 1,
#         else:
#             s.append(a[j]+a[j-1])
#             print a[j]+a[j-1],
#     print
#     a,s = s,[]

#输入三个数字,按照大小顺序输出.使用max函数输出列表中最大的值,使用remove函数再删除列表中最大值
# if __name__=='__main__':
#     l=[]
#     for i in range(3):
#         x=raw_input('输入一个数字:')
#         l.append(x)
#     for i in range(3):
#         print(max(l))
#         l.remove(max(l))                                                                                                 #利用 remove（）函数依次输出最大值

#有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数,注意extend()函数是用新列表扩展原来的列表,所以是在原列表的基础上变化,使用扩展后的列表用原列表的变量名即可

# n = input("请输入整数数量:")
# x = input("请输入向后移动的位数:")
# a =[]
# for i in range(n):
#     b = input("请输入一个整数:")
#     a.append(b)
# c = a[n-x:]
# d = a[:n-x]
# e = c.extend(d)
# print c

#有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

# n=int(input("请输入人数:"))
# List=[]
# for i in range(1,n+1):
#     List.append(i)
#
# sum=0
# while 1:
#     t = 0
#     for i in range(1,len(List)+1):
#         sum=sum+1
#         if (sum)%3==0:
#             List.pop(i-1-t)
#             t=t+1
#
#     if len(List)==1:
#         print("最后留下的是原来第%d号的那位" % List[0])
#         break

#该方法还是删除列表中的第三个元素,不过实现方法是通过while循环实现,以及pop()和insert()函数,大致思路是第一和二次循环,删除首元素,同时将首元素插入到尾部,第三次循环时删除首元素,即删除原数列的第三个元素
#而且该方式删除后效果如下方法三相同逻辑

# data = [i+1 for i in range(n)]
# i = 1
# while len(data) > 1:
#     if i % 3 == 0:
#         data.pop(0)
#         print data
#     else:
#         data.insert(len(data),data.pop(0))
#         print data
#     i += 1

# print(data)

#方法三,该方法是将一个数列分成1,2,3多个这种小模块来实现的,如[1,2,3,4,5]看成[1,2,3]和[4,5],然后将列表中第三个元素去除,再下一次循环前,将[4,5]放在[1,2]之前,相当于[4,5]依然为[1,2]
#而删除第三个元素后的[1,2]实际上变为[3,4],作为环形队列的另一种实现

# a=[]
# for i in range(1,n+1):
#     a.append(i)
# b=deque(a)                                                                                                      #使用双段队列deque,目的是使用里面的方法回转rotate
# while True:                                                                                                     #创建删除符合3的数并且回转列表
#     print b
#     b.remove(b[2])                                                                                              #删除为3的数也就是索引为2的数
#     b.rotate(-2)                                                                                                #将第三个数后面的数进行回转从头开始
#     if len(b)==2:
#         print b
#         print b[1]                                                                                              #最后剩两个数，那么最后的人一定是最后一个数
#         break

#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n.这里注意一点就是b中1.0要必须是float类型,不然整型会自动去除小数点后的数字

# n = input("请输入一个整数:")
#
# def even(n):
#     a = 0
#     for i in range(1,n / 2 + 1):
#         b = 1.0 / (2 * i)
#         a += b
#     print a
#
# def odd(n):
#     a = 0
#     for i in range((n+1)/2):
#         a += 1.0 / (1 + 2 * i)
#     print a
#
# if __name__ == "__main__":
#     if n % 2 == 0:
#         even(n)
#     elif n % 2 != 0 :
#         odd(n)
#     else:
#         print "输入有误,请重新输入"

#找到年龄最大的人，并输出.该题最重要的是是根据键值查找相对应的键,介绍下字段的两个内置函数items和iteritems函数,items()方法是将字典中的每个项分别做为元组，添加到一个列表中，形成了一个新的列表容器
#iteritems与items方法相比作用大致相同，只是它的返回值不是列表，而是一个迭代器

# person = {"li":18,"wang":50,"zhang":20,"sun":22}
# k = person.values()
# a = max(k)
# ps = {v:k for k,v in person.items()}                                 #注意该方式,该方法是利用原字典创建新字典的方法,而采用这种方式来根据键值查找键,其实就是创建了一个与原字典
# print ps                                                             #键值与键相反的新字典,然后再根据键值查询.其实根本还是根据键查找键值
# print ps[a]
#
# for key,value in person.iteritems():                                 #该方式是通过循环出字典中所有的键和键值,然后分别将查询出的键值与a键值比较
#     if value == a:
#         print key

#字符串排序,字符串排序是先根据首字母比较,如果相同再进行下一个字母的比较
#sort和sorted的区别是list的sort方法返回的是对已经存在的列表进行操作，而内建函数sorted方法返回的是一个新的list，而不是在原来的基础上进行的操作

# if __name__=='__main__':
#     ls=[]
#     str1 = raw_input("string1:\n")
#     str2 = raw_input("string2:\n")
#     str3 = raw_input("string3:\n")
#     ls.extend([str1,str2,str3])
#     # ls.sort()
#     list2=sorted(ls)                                #sorted() 函数对所有可迭代的对象进行排序操作
#     print(list2)

#猴子分桃问题,每次都把上个猴子剩下的桃子分成5份,最后多了一个
#
# if __name__ == '__main__':
#     i = 0
#     j = 1
#     x = 0
#     while (i < 5) :
#         x = 4 * j
#         for i in range(0,5) :
#             if(x%4 != 0) :
#                 break
#             else :
#                 i += 1
#             x = (x/4) * 5 +1
#         j += 1
#     print x

# 猴子分桃，最少问题分析：问最少有多少只桃子，则岸上最后剩的桃子数目越小，则原岸上的桃子越少
# 假设最后岸上还剩4x只桃子,可以利用递归方法求解

# num = int(input("输入猴子的数目:"))
#
#
# def fn(n):
#     if n == num:
#         return (4 * x)  # 最后剩的桃子的数目
#     else:
#         return (fn(n + 1) * 5 / 4 + 1)
#
#
# x = 1
# while 1:
#     count = 0
#     for i in range(1, num):
#         if fn(i) % 4 == 0:
#             count = count + 1
#     if count == num - 1:
#         print("海滩上原来最少有%d个桃子" % int(fn(0)))
#         break
#     else:
#         x = x + 1

#求0—5所能组成的奇数个数,思考怎么将这种代码简化,更加动态的编写

# a = 0
# for i in range(5):
#     if i % 2 != 0:
#         a += 1
#
# for m in range(1,5):
#     for n in range(5):
#         if (m*10+n) % 2 != 0:
#             a += 1

#连接字符串,注意该join方法的使用,该方法用于将序列中的元素以指定的字符连接生成一个新的字符串,所以如果需要加一个列表中的元素显示出来,可以使用for循环，也可以使用该方式，将多个空格连接每个元素即可显示

# delimiter = '  '
# list = ['Brazil', 'Russia', 'India', 'China']
# print list
# print delimiter.join(list)

#输入一个奇数，然后判断最少几个9除于该数的结果为整数,方法一,这里最重要的一点是用while循环来实现,且这里采用字符串方式处理多个9的增加

# def opinion(n):
#     a = 9
#     b = 1
#     if 9 % n == 0:
#         print '1个9可以被%d整除' % (n)
#     else:
#         while b == 1:
#             if int(a) % n == 0:
#                 print '%d个9可以被%d整除' % (len(a), n)
#                 b = 2
#             else:
#                 a = str(a) + '9'
#                 b = 1
#
# if __name__ == "__main__":
#     n = input("请输入一个奇数:")
#     if n % 2 == 0:
#         print "不可以输入偶数"
#     else:
#         opinion(n)

#方法二,采用两个变量的增加来实现多个9的增加变化,如下的m9和sum两个变量实现了每次循环后的999的增加为9999等变化.这里特别学习注意下这种多个变量的变化实现一个有规律的数列变化
# if __name__ == '__main__':
#     zi = int(raw_input('输入一个数字:\n'))
#     n1 = 1
#     c9 = 1
#     m9 = 9
#     sum = 9
#     while n1 != 0:
#         if sum % zi == 0:
#             n1 = 0
#         else:
#             m9 *= 10
#             sum += m9
#             c9 += 1
#     print '%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum)
#     r = sum / zi
#     print '%d / %d = %d' % (sum,zi,r)

#方法三,该方式最简洁,在编写时一定要先找出一个有规律数列的最简单实现的方法逻辑
# b=input('input a number:\n')
# a=9
# n=1
# while (1):
#     if a % b==0:
#         break
#     else:
#         a=a*10+9
#         n=n+1
# print '%d 个 9 除于 %d 为整数' % (n,b)

#读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊

# for j in range(7):
#     n = random.randint(1, 50)
#     for i in range(n):
#         if i == n-1:
#             print '*'
#         else:
#             print '*',

#一个四位整数,每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换.方法一将输入的整数当成字符串处理

# n = raw_input("请输入一个四位整数:")
# a = n[0]
# b = n[1]
# c = n[2]
# d = n[3]
# a = (int(a)+5) % 10
# b = (int(b)+5) % 10
# c = (int(c)+5) % 10
# d = (int(d)+5) % 10
# x = str(d) + str(c) + str(b) + str(a)
# print x

#方法二,通过运算符的操作得到一个整数的个位、十位等位置上的数字,这里注意使用range方式来倒序显示一个列表,即效果与list.reverse()方法相同
#这里使用stdout.write()方法,与print()方法的区别,Python 中打印对象调用print obj时候，事实上是调用了 sys.stdout.write(obj+'\n').换句话说print()方法调用实际上是调用了sys.stdout的write 方法
# if __name__ == '__main__':
#     a = int(raw_input('输入四个数字:\n'))
#     n = []
#     n.append(a % 10)
#     n.append(a % 100 / 10)
#     n.append(a % 1000 / 100)
#     n.append(a / 1000)
#
#     for i in range(4):
#         n[i] += 5
#         n[i] %= 10
#
#     for i in range(2):
#         n[i],n[3 - i] = n[3 - i],n[i]
#
#     for i in range(3,-1,-1):                                                                                             #代表3到-1,间隔为-1(不包括-1)
#         stdout.write(str(n[i]))

#time clock()函数以浮点数计算的秒数返回当前的CPU时间.用来衡量不同程序的耗时,比time.time()更有用.注意该方法在不同的系统上含义不同.在UNIX系统上,它返回的是"进程时间",它是用秒表示的浮点数(时间戳)
# if __name__ == '__main__':
#     start = time.clock()
#     for i in range(3000):
#         print i
#     end = time.clock()
#     print 'different is %6.3f' % (end - start)
#
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(3000):
#         print i
#     end = time.time()
#     print end - start

#一个猜数游戏，判断一个人反应快慢

# r = random.randint(1,1000)
# a = 1
# start = time.time()
# while a:
#     print r
#     n = input("请输入所猜数字(1到1000范围内):\n")
#     if r == n:
#         end = time.time()
#         print 'You guess is %d' % (n)
#         print 'Congradulations,you guess right! and you elapsed time is %f' % (end - start)
#         break
#     elif r < n:
#         print 'Please input smaller number'
#         a = 1
#     elif r > n:
#         print 'Please input bigger number'
#         a = 1
#     else:
#         print 'Please input correct number'
#         a = 1

#计算字符串中子串出现的次数

# a = "abssafasdawuioeqadbab"
# b = "ab"
# print a.count(b)

#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
#
# fo = open("fool.txt","a+")
# a = 1
# while a:
#     n = raw_input("请输入需要写入文件的字符:\n")
#     if n == '#':
#         print "写入结束"
#         break
#     else:
#         fo.write(n + "\n")                                                                                      #每次写入的时候都换行
#         a = 1

#有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中

# fo = open("test1.txt","r")
# a = fo.read()
# fo.close()
# fo = open("test2.txt","r")
# b = fo.read()
# fo.close()
# fo = open("test3.txt","w")
# c = list(a + b)
# c.sort()
# d = '  '.join(c)
# fo.write(d)
# fo.close()

#列表转换为字典,这里特别注意下zip函数的使用,该函数将接受一系列可迭代的对象作为参数,将对象中对应的元素打包成一个个tuple(元组),然后返回由这些tuples组成的list(列表).若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同
#实际zip函数的效果如下所示,如果该该函数有多个参数,则将两个列表中对应的元素组成一个元组存放在列表中.dict()方法是将一个数列转换成字典类型.dict()函数的两种使用情况方法如下所示

#方法一
# x = ['siri', 'bibxy']
# y = [12, 56]
# print dict([x])

#方法二,使用zip函数操作多个可迭代的对象
# i = ['a','b','c']
# l = [1,2,3]
# a = zip(i,l)
# print a
# b=dict(a)
# print(b)

#方法三,使用字典的setdefault()函数
# l1 = ['a','b','c']
# l2 = [1,2,3]
# d = {}
# for i in range(len(l1)):
#     d.setdefault(l1[i],l2[i])
# print d

#方法四,这里注意写法问题,这种写法是python的语法糖写法,多学习下这类写法
# keys = ['a', 'b']
# values = [1, 2]
# print({keys[i]: values[i] for i in range(len(keys))})

#将一个正整数分解质因数

# n = input("请输入一个整数:")
# a = 1
# while a == 1:
#     for i in range(2,n+1):
#         if i < n and n % i == 0:
#             print i
#             n = n / i
#             a = 1                                                         #将n循环%i的值,如果能够整除,那么将n/i的值赋给n,然后设a=1可以继续while循环,从而继续运行for循环
#             break
#         elif i == n:                                                      #如果i == n了,那么说明该n的值不能再继续分解了,即可以设a=2退出循环了
#             print n
#             a = 2
#             break
#         else:                                                             #该else是在n%i的值不为0的情况下,是为了将for循环进行下去,一直到找到其他两个条件下的语句中运行
#             continue

#有一组"+"和"-"符号,要求将"+"排到左边,"-"排到右边
# def test(data):
#     start = 0
#     end = 0
#     count = len(data)
#     while (start + end) < count :
#         if data[start] == '-':
#             data[start],data[count-end-1] = data[count-end-1],data[start]
#             end += 1
#         else:
#             start += 1
#     print(data)
# if __name__ == "__main__":
#     data =  ['+', '-', '+', '+', '+','-', '+','-', '+','-','-']
#     test(data)
