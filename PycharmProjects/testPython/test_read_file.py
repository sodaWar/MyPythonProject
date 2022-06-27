# -*- coding:utf-8 -*-
import traceback
import linecache
import sys

try:
    a = 1 / 0
    print(a)  # 捕获异常并使用traceback异常模块来输出详细的异常信息
except (ZeroDivisionError, AttributeError) as e:
    traceback.print_exc(file = open('D:/test_file/test_excep.txt', 'w+'))
    try:                                        #读取文件内容，因为读写过程中可能产生IOError异常，所以使用try和finally来实现，注意文件open后一定要close
        test_excep = "D:/test_file/test_excep.txt"
        t_e = open(test_excep, "r")
        print(t_e.read())
    except IOError as e:
        print(("IOError:", e))
    finally:
        test_excep = "D:/test_file/test_excep.txt"
        t_e = open(test_excep, "r")
        if t_e:
            t_e.close()

    test_excep = "D:/test_file/test_excep.txt"                #使用read()方式读取文件内容，这个是对以上代码的简写，使用with open...as...方式
    with open(test_excep,"r") as t_e:
        print (t_e.read())
        t_e.close()
        print (t_e.closed,t_e.mode,t_e.name)

    test_excep = "D:/test_file/test_excep.txt"
    with open(test_excep,"r") as t_e:                 #使用readlines()方式可以一次读取所有内容并按行返回list
        te_list = t_e.readlines()               #注意，readline()方式是每次读取一行内容
        print (type(te_list))
        for i in te_list:
            print (i+".................", )

    test_excep = "D:/test_file/test_excep.txt"
    count = len(open(test_excep,"rU").readlines())          #获取文件的行数
    print (count)
    for i in range(count):
        line_content = linecache.getline(test_excep,i+1)           #该代码可以指定读取文件中某一行的内容，getline方法是读取文件某一行的内容
        print (i)
        print (line_content)

    test_excep = "D:/test_file/test_excep.txt"
    str = linecache.getlines(test_excep)            #getlines方法是读取文件整个文本内容，但是返回的值是列表形式，因此可以指定下表访问某一行的内容
    print (str[2])

try:
   raise ZeroDivisionError     #自抛异常
except ZeroDivisionError:
   traceback.print_exc()

name = input("Enter you name:")      #raw_input方式获取用户输入的信息内容
print (name)

data = sys.stdin.readline().strip('\n')   #strip函数是用于移除字符串头尾指定的字符，默认为空格，如果字符串中间包含该字符不会被移除
print(len(data))
for i in range(len(data)):
    print (data[i] + 'hello')
#sys.stdin.readline()方法获取输入时返回的结果会包括末尾的换行符，所以其字符长度显示会比输入长度大1
#raw_input（）方法会返回不包括末尾的换行符

try:
    a = 1/0                   #回溯异常
    print (a)
except ZeroDivisionError as e:
    info = sys.exc_info()
    print (info[0],":",info[1],":",info[2])

