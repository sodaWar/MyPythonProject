# 第一题
# a = input()
# b = a.split(' ')
# print(len(b[-1]))

# 第二题
# a = input()
# b = input()
# c = a.lower().count(b.lower())   # lower()全部转换成小写
# print(c)

# 第三题
import numpy as np
import random
# a = input()
# c = []
# for i in range(int(a)):
#     d = input()
#     if d not in c:
#         c.append(d)
# d = []
# for x in c:
#     d.append(int(x))
# d.sort()            # 升序作用
# for y in d:
#     print(y)
# np.array（）作用是把我们定义的普通数组转化为Numpy中的array类型，这样做的好处就在于可以使用该类型定义的多种数组方法
# 比如排序取其中的最大值或者最小值。我们就不需要从头开始实现，直接调用相关的API就行。
# d = np.array(c)
# print(np.unique(d, axis=0))  # 该函数有数组去重和升序作用

# 第四题
# import re
# a = input()
# c = a
# if len(a) <= 8:
#     b = 8 - len(a)
#     for i in range(b):
#         c = c + '0'
#     print(c)
# else:
#     d = int(len(a)/8)
#     e = len(a) - 8*d
#     if e == 0:
#         f = ''
#     else:
#         f = a[-e:]
#         b = 8 - e
#         for i in range(b):
#             f = f + '0'
#     g = re.findall(r'\w{8}', a)
#
#     g.append(f)
#     for x in g:
#         print(x)

# 第五题
# a = input()
# b = a[2:]
# c = []
# if b[0] == 'A':
#     d = 10
# elif b[0] == 'B':
#     d = 11
# elif b[0] == 'C':
#     d = 12
# elif b[0] == 'D':
#     d = 13
# elif b[0] == 'E':
#     d = 14
# elif b[0] == 'F':
#     d = 15
# else:
#     d = b[0]
#
# for i in range(1, len(b)):
#     if b[-i] == 'A':
#         c.append(10)
#     elif b[-i] == 'B':
#         c.append(11)
#     elif b[-i] == 'C':
#         c.append(12)
#     elif b[-i] == 'D':
#         c.append(13)
#     elif b[-i] == 'E':
#         c.append(14)
#     elif b[-i] == 'F':
#         c.append(15)
#     else:
#         c.append(int(b[-i]))
# c.append(int(d))
# f = 0
# for i in range(len(c)):
#     f += c[i] * 16**i
# print(f)
# 以下是网络上简洁的写法，主要是利用了字典key:value的写法
# while True:
#     try:
#         number = input()
#         n = len(number)
#         dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
#         final = 0
#         for i in range(2,n):
#             print(dic[number[i]])
#             final += dic[number[i]]*(16**(n-i-1))
#         print(final)
#     except:
#         break

# 第六题
# a = input()
# b = a.split(' ')
# print(len(b[-1]))

# 第七题
# a = input()
# b = input()
# c = a.lower().count(b.lower())
# print(c)

# 第八题：质数因子，需要多次查看写法和逻辑
# n=int(input())
# def fn(n):
#     for i in range(2,n+1):
#         if n%i==0:
#             if n//i==1:
#                 print(i,end=' ')
#                 break
#             print(i,end=' ')
#             n=n//i
#             fn(n)
#             break
# fn(n)

# 第九题
# a = input()
# b = a.split('.')
# c = '0.'+b[1]
# d = 0
# if float(c) >= 0.5:
#     d = int(b[0]) + 1
# else:
#     d = int(b[0])
# print(d)

# 第十题
# count = int(input())
# dic = {}
# for i in range(count):
#     line = input().split()  # 输入相应的行
#     key = int(line[0])   # 将输入的行的第一个字符作为字典的键
#     value = int(line[1])  # 将输入的行的第一个字符作为字典的值
#     if key in dic:
#         dic[key] += value  # 判断如果对应键的值在字典中，就将该键的对应的值相加
#     else:
#         dic[key] = value    # 判断如果对应键的值不在字典中，就将该键的对应的值添加
# for j, k in sorted(dic.items()):  # 对字典进行升序，然后取且相应的键值
#     print(j, k)

# 第十一题
# a = input()
# b = ''
# for i in range(1, len(a)):
#     b += a[-i]
# c = b+a[0]
# d = []
# e = ''
# for x in c:
#     if x not in d:
#         d.append(x)
# for y in d:
#     e += y
# print(int(e))

# 第十二题
# a = input()
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(len(b))

# 第十三和十四题
# a = input()
# b = ''
# for i in range(1, len(a)):
#     b += a[-i]
# c = b + a[0]
# print(c)

# 第十五题
# a = input()
# b = a.split(' ')
# c = []
# for i in range(1, len(b)):
#     c.append(b[-i])
# c.append(b[0])
# e = ''
# for x in c:
#     if x == c[0]:
#         e += x
#     else:
#         e += ' ' + x
# print(e)

# 第十六题
# a = input()
# b = []
# for i in range(int(a)):
#     b.append(input())
# c = sorted(b)
# for x in c:
#     print(x)

# 第十七题
# a = int(input())
# b = ''
# if a == 0:
#     print(0)
# elif a == 1:
#     print(1)
# else:
#     while a != 1:
#         b += str(a % 2)
#         a = a // 2
#     c = ''
#     for i in range(1, len(b)):
#         c += b[-i]
#     d = '1' + c + b[0]
#     print(d.count('1'))

# 第十八题
# def test(i):
#     b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     if len(i) == 3 and i[1] not in b:
#         return i
#     elif len(i) == 3 and i[2] not in b:
#         return i
#     elif i[0] != 'A' and i[0] != 'W' and i[0] != 'S' and i[0] != 'D':
#         return i
#     elif len(i) > 3 or len(i) == 1:
#         return i
#     elif len(i) == 2 and i[1] not in b:
#         return i
#     else:
#         return 1
#
# num = input()
# num_a = num.split(';')
# while '' in num_a:
#     num_a.remove('')
# num_b = []
# for i in num_a:
#     num_b.append(test(i))
# while 1 in num_b:
#     num_b.remove(1)
# for y in num_b:
#     if y in num_a:
#         num_a.remove(y)
#
# a = 0
# b = 0
# for m in num_a:
#     if m[0] == 'A':
#         a -= int(m[1:])
#     elif m[0] == 'D':
#         a += int(m[1:])
#     elif m[0] == 'S':
#         b -= int(m[1:])
#     elif m[0] == 'W':
#         b += int(m[1:])
# c = str(a) + ',' + str(b)
# print(c)

# 第十九题
# import re
# def test_bigzimu(password):
#     b = 0
#     for i in password:
#         if re.match('^[A-Z]+$', i):
#             b = 1
#         else:
#             continue
#     return b
#
# def test_smallzimu(password):
#     b = 0
#     for i in password:
#         if re.match('^[a-z]+$', i):
#             b = 1
#         else:
#             continue
#     return b
#
# def test_suzi(password):
#     b = 0
#     for i in password:
#         if i.isdigit():
#             b = 1
#         else:
#             continue
#     return b
#
# def test_tesuzf(password):
#     if re.search(r"\W", password):
#         return 1
#     else:
#         return 0
#
#
# def test_dup(password):
#     b = []
#     for i in range(3, len(password)):
#         c = password
#         for x in range(len(c) - i):
#             b.append(c[0:i])
#             if len(c[1:]) == i:
#                 b.append(c[1:])
#             else:
#                 c = c[1:]
#
#     d = set(b)
#     if len(d) == len(b):
#         return 1
#     else:
#         return 0
#
# def test_one(password):
#     number_one = test_tesuzf(password) + test_suzi(password) + test_bigzimu(password) + test_smallzimu(password)
#     if len(password) <= 8:
#         return False
#     elif re.search("\s", password) or re.search("\n", password):
#         return False
#     elif number_one < 3:
#         return False
#     elif test_dup(password) == 0:
#         return False
#     else:
#         return True
#
# while 1:
#     try:
#         a = input()
#         if test_one(a):
#             print('OK')
#         else:
#             print('NG')
#     except EOFError:
#         break

# 第十九题网上答案
# def check():
#     # 输入一组字符串
#     string = input()
#     # 条件1:长度超过8
#     if len(string) <= 8: return 0
#     # 条件2：小写字母、大写字母、数字、特殊符号，必须至少包含3种
#     a, b, c, d = 0, 0, 0, 0
#     for i in string:
#         if 'a' <= i <= 'z':
#             a = 1
#         elif 'A' <= i <= 'Z':
#             b = 1
#         elif '0' <= i <= '9':
#             c = 1
#         else:
#             d = 1
#     if a + b + c + d < 3: return 0
#     # 条件3：重复子串的长度不能大于2
#     dic = {}
#     for i in range(len(string) - 3):
#         subString = string[i:i + 3]
#         if subString not in dic:
#             dic[subString] = 1
#         else:
#             dic[subString] += 1
#             if dic[subString] >= 2: return 0
#     return 1
#
#
# while True:
#     try:
#         if check():
#             print("OK")
#         else:
#             print("NG")
#     except:
#         break

# 第二十题
# import re
# number = input()
# dic = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5',
#        'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8', 'v': '8',
#        'w': '9', 'x': '9', 'y': '9', 'z': '9'}
# a = ''
# for i in number:
#     if re.match('^[A-Y]+$', i):
#         a += chr(ord(i.lower())+1)
#     elif re.match('^[Z]+$', i):
#         a += 'a'
#     elif re.match('^[a-z]+$', i):
#         a += dic[i]
#     else:
#         a += i
# print(a)

# 第二十一题
# def test(no_bottle):
#     drink_bottle = 0
#     while no_bottle >= 3:
#         right_bottle = no_bottle // 3
#         drink_bottle += right_bottle
#         left_bottle = no_bottle % 3
#         no_bottle = left_bottle + right_bottle
#     if (no_bottle == 2):
#         drink_bottle += 1
#         print(drink_bottle)
#     else:
#         print(drink_bottle)
#
# while 1:
#     try:
#         no_bottle = int(input())
#         if no_bottle == 0:
#             break
#         else:
#             test(no_bottle)
#     except:
#         break

# 第二十二题
# a = input()
# b = []
# for i in a:
#     b.append(a.count(i))
# c = min(b)
# d = []
# for x in range(len(a)):
#     if a.count(a[x]) == c:
#         d.append(x)
#     else:
#         continue
# e = ''
# for x in range(len(a)):
#     if x not in d:
#         e += a[x]
#     else:
#         continue
# print(e)
# 以下是一开始的写法，比较死板
# e = []
# f = []
# g = []
# for m in a:
#     e.append(m)
# for n in d:
#     f.append(e[n])
# # 该代码更简介，一个列表删除另外一个列表的数据
# g = [x for x in e if x not in f]
# # for item in e:
# #     if item not in f:
# #         g.append(item)
# #     else:
# #         continue
#
# h = ''
# for x in g:
#     h += x
# print(h)

# 以下是网络上的好方法，用字典来实现
# while True:
#     try:
#         s = input()
#         dic, res = {}, ''
#         for c in s:
#             if c not in dic:
#                 dic[c] = 1
#             else:
#                 dic[c] += 1
#         Min = min(dic.values())
#         for c in s:
#             if dic[c] != Min:
#                 res += c
#         print(res)
#     except:
#         break

# 第二十三题
# while True:
#     try:
#         s = input()
#         a = ''
#         for i in s:
#             if i.isalpha():
#                 a += i
#         b = sorted(a, key=str.lower)
#         index = 0
#         d = ''
#         for i in range(len(s)):
#             if s[i].isalpha():
#                 d += b[index]
#                 index += 1
#             else:
#                 d += s[i]
#         print(d)
#     except:
#         break

# 第二十四题
# while True:
#     try:
#         s = input().split()
#         dic = s[1:-2]
#         x = s[-2]
#         k = int(s[-1])
#         brother = []
#         # 这里最快捷的解题思路是，不管他们怎么变化顺序，里面的字母是没变的，所以给他们排个序，作比较就行了！不用傻乎乎的，去把所有的兄弟单词数量列举出来，
#         # 然后再跟现有的单词比较！只要比较两个单词字母都相同，只是顺序不同就行了！
#         for i in dic:
#             if sorted(i) == sorted(x) and i != x:
#                 brother.append(i)
#         brother = sorted(brother)
#         print(len(brother))
#         print(brother[k-1])
#     except:
#         break

# 第二十五题
# import re
# def jiami(number):
#     a = ''
#     for i in number:
#         if re.match('^[A-Y]+$', i):
#             b = i.lower()
#             a += chr(ord(b)+1)
#         elif re.match('^[a-y]+$', i):
#             b = i.upper()
#             a += chr(ord(b)+1)
#         elif i == 'Z':
#             a += 'a'
#         elif i == 'z':
#             a += 'A'
#         elif i != '9' and i.isdigit():
#             a += str(int(i) + 1)
#         elif i == '9':
#             a += '0'
#         else:
#             continue
#     print(a)
#
# def jiemi(number):
#     a = ''
#     for i in number:
#         # print(i)
#         if re.match('^[B-Z]+$', i):
#             b = i.lower()
#             a += chr(ord(b)-1)
#         elif re.match('^[b-z]+$', i):
#             b = i.upper()
#             a += chr(ord(b)-1)
#         elif i == 'A':
#             a += 'z'
#         elif i == 'a':
#             a += 'Z'
#         elif i != '0' and i.isdigit():
#             a += str(int(i) - 1)
#         elif i == '0':
#             a += '9'
#         else:
#             continue
#     print(a)
#
# number = input()
# number_2 = input()
# jiami(number)
# jiemi(number_2)

# 第二十六题
# print(int("0011", 2))  # 后面参数是当前数据的进制，只转换成10进制，也就是2进制转换成10进制
# print(bin(8))  # 10进制转换成2进制
# print(str(hex(eval('14'))))     # 10进制转换成16进制
# print(oct(50))      # 10进制转换成8进制
import numpy
# def test_one(number_one):
#     jishu = []
#     oushu = []
#     number_two = ''
#     for i in range(len(number_one)):
#         if (i+1) % 2 != 0:
#             jishu.append(number_one[i])
#         else:
#             oushu.append(number_one[i])
#     jishu_two = sorted(jishu)
#     oushu_two = sorted(oushu)
#     if len(jishu_two) > len(oushu_two):
#         oushu_two.append('')
#     number_three = list(zip(jishu_two, oushu_two))
#     for i in range(len(number_three)):
#         number_two += number_three[i][0] + number_three[i][1]
#     return number_two
#
# def zimu():
#     # aa = numpy.arange(97, 123)
#     # AA = numpy.arange(65, 91)
#     a = []
#     A = []
#     for i in range(97, 103):
#         a.append(chr(i))
#     for i in range(65, 71):
#         A.append(chr(i))
#     b = {}
#     c = {}
#     x = 10
#     for i in a:
#         b[i] = x
#         x += 1
#
#     y = 10
#     for i in A:
#         c[i] = y
#         y += 1
#     b.update(c)
#     return b
#
# def change(number_ten):
#     if number_ten >= 8:
#         change_one = bin(number_ten)[2:]
#     elif number_ten == 1 or number_ten == 0:
#         change_one = '000' + bin(number_ten)[2:]
#     elif number_ten == 2 or number_ten == 3:
#         change_one = '00' + bin(number_ten)[2:]
#     else:
#         change_one = '0' + bin(number_ten)[2:]
#     a = ''
#     b = change_one[0]
#     for i in range(1, len(change_one)):
#         a += change_one[-i]
#     a += b
#     c = int(a, 2)
#     d = str(hex(c))
#     e = d[2:].upper()
#     return e
#
# def test_two(number_temp):
#     number_temp2 = []
#     number_temp3 = zimu()
#     a = number_temp3.keys()
#     for i in range(len(number_temp)):
#         if number_temp[i] in a:
#             number_temp2.append(number_temp3[number_temp[i]])
#         elif number_temp[i].isdigit():
#             number_temp2.append(int(number_temp[i]))
#         else:
#             number_temp2.append(number_temp[i])
#     result_one = ''
#     for m in number_temp2:
#         if type(m) == int:
#             result_one += change(m)
#         else:
#             result_one += m
#     return result_one
#
# m = input()
# n = m.split(' ')
# x = ''
# for i in n:
#     x += i
# y = test_one(x)
# result = test_two(y)
# print(result)


# 输入字典中的所有值的两种方法
# print("Value : %s" % b)
# for key, values in c.items():
#     print(key)
#     print(values)

# 第二十七题
# small_zimu = []
# big_zimu = []
# for i in range(65, 91):
#     big_zimu.append(chr(i))
# for i in range(97, 123):
#     small_zimu.append(chr(i))
# all_zimu = small_zimu + big_zimu
# number = input()
# a = ''
# for i in number:
#     if i in all_zimu:
#         a += i
#     else:
#         a += ' '
# b = a.strip()
# c = b.split(' ')
# d = c[0]
# e = []
# for m in range(1, len(c)):
#     e.append(c[-m])
# e.append(d)
# f = ''
# for x in e:
#     f += x + ' '
# g = f.rstrip()
# print(g)

# 第二十八题
# number = input()
# a = sorted(number)
# b = ''
# for i in a:
#     b += i
# print(b)

# 第二十九题
# import re
# def change_one(number_one):
#     a = number_one.split('.')
#     e = ''
#     for i in a:
#         c = bin(int(i))[2:]
#         d = ''
#         if len(c) < 8:
#             for x in range(8 - len(c)):
#                 d += '0'
#             d += c
#         else:
#             d = c
#         e += d
#     result = int(e, 2)
#     print(result)
#
# def change_two(number_two):
#     a = bin(int(number_two))[2:]
#     b = a.rjust(32, '0')
#     c = re.findall(r'.{8}', b)
#     d = ''
#     for i in c:
#         d += str(int(i, 2)) + '.'
#     e = d[0:-1]
#     print(e)
#     return e
#
# number_one = input()
# number_two = input()
# change_one(number_one)
# change_two(number_two)

# 以下是网上的答案，更简洁，请参考
# def transfer_ip2num(ip):
#     ip_list = ip.split('.')
#     bin_str = ''
#     for x in ip_list:
#         bin_str += bin(int(x))[2:].rjust(8,'0')
#     return int(bin_str, 2)
# print(transfer_ip2num(input()))


# 第三十题
# 方法一
# while True:
#     try:
#         m = int(input())
#         for i in range(1, m + 1):
#             for j in range(1, m - i + 2):
#                 if j == m - i + 1:
#                     print((i + j - 2) * (i + j - 1) // 2 + j)
#                 else:
#                     # 为末尾end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串，
#                     # 其实这也是一个语法要求，表示这个语句没结束。不然print函数会默认结束语句并换行
#                     print((i + j - 2) * (i + j - 1) // 2 + j, end=' ')
#     except:
#         break

# 方法二
# 观察第一行的规律符合累加求和公式；(n+1)n/2
# 第二行的规律则是第一行的 ((n+1)n/2) - 1
# 第三行的规律则是第一行的 ((n+1)n/2) - 2
# 当i = 1 时，j = 1,2,3,4 进入循环；
# 当i = 2 时，j = 2,3,4
# n = int(input().strip())
# for i in range(1, n+1):
#     for j in range(i, n+1):
#         print(int(((j+j**2)/2)-i+1), end=' ')
#     print()

# 方法三(自己写,找到每一行数据的规律，第二行是第一行数据减去第一个数据之后，再每个值都减去1的结果；第三行是第一行数据
# 减去前两个数据之后，再每个值都减去2个结果，这样只要得到第一行数据列表，后面就可以算出来了)
# n = int(input().strip())
# a = []
# for i in range(1, n+1):
#     b = 0
#     for x in range(1, i+1):
#         b += x
#     a.append(b)
#
# for i in range(1, n+1):
#     c = ''
#     if i == 1:
#         for m in a:
#             c += str(m) + ' '
#         print(c)
#     else:
#         b = a[i-1:]
#         for x in b:
#             c += str((int(x)-i+1)) + ' '
#         print(c)

# 第三十一题
# def jm_key(key):
#     a = ''
#     for i in key:
#         if i not in a:
#             a += i
#     b = []
#     for i in range(97, 123):
#         b.append(chr(i))
#     c = []
#     for i in b:
#         if i not in a:
#             c.append(i)
#         else:
#             continue
#     d = list(a)
#     d.extend(c)
#     e = list(zip(b, d))
#     g = {}
#     for i in range(len(e)):
#         g[e[i][0]] = e[i][1]
#     return g
#
# n_one = input()
# n_two = input()
# g = jm_key(n_one)
# a = ''
# for i in n_two:
#     a += g[i]
# print(a)

# 第三十二题
# n = int(input())
# a = [1, 1]
# for i in range(n-2):
#     b = a[i] + a[i+1]
#     a.append(b)
#
# print(a[n-1])

# 第三十四题
# n = int(input())
# all_n = n + n + n/2 + n/4+n/8
# ft_n = n/32
# print(all_n)
# print(ft_n)

# 第三十五题
# def change(number):
#     a = number.split('.')
#     b = []
#     for i in a:
#         c = bin(int(i))[2:].rjust(8, '0')
#         b.append(c)
#     return b
#
# def change_two(number_one, number_two):
#     a = ''
#     for i in range(len(number_one)):
#         for m in range(len(number_one[i])):
#             if int(number_one[i][m]) + int(number_two[i][m]) == 2:
#                 a += '1'
#             else:
#                 a += '0'
#     return a
#
# def jy(number):
#     a = number.split('.')
#     for i in a:
#         if int(i) < 0 or int(i) > 255:
#             return 0
#         else:
#             continue
#
# def main():
#     yanma = input()
#     ip_one = input()
#     ip_two = input()
#     if jy(yanma) == 0 or jy(ip_one) == 0 or jy(ip_two) == 0:
#         print(1)
#         return 1
#     yanma_2 = change(yanma)
#     ip_one_2 = change(ip_one)
#     ip_two_2 = change(ip_two)
#     if yanma_2[0] != '11111111' or yanma_2[-1] != '00000000':
#         print(1)
#         return 1
#     result_one = change_two(yanma_2, ip_one_2)
#     result_two = change_two(yanma_2, ip_two_2)
#     if result_one == result_two:
#         print(0)
#         return 0
#     else:
#         print(2)
#         return 2
#
# main()

# 第三十六题
# a = input()
# yw = 0
# kg = 0
# sz = 0
# qt = 0
# for i in a:
#     if i.isdigit():
#         sz += 1
#     elif i.isalpha():
#         yw += 1
#     elif i == ' ':
#         kg += 1
#     else:
#         qt += 1
# print(yw)
# print(kg)
# print(sz)
# print(qt)

# 第三十七题
# 相当于在（1,1,2,3,3,3,3）这个列表中，求得所有的相加的结果种类，数据不能重复而已！也就是找全组合数量，另外不重复
from copy import deepcopy
# zl = input()
# weight = input()
# number = input()
# a = []
# number_one = number.split(' ')
# weight_one = weight.split(' ')
# for i in range(len(number_one)):
#     for x in range(int(number_one[i])):
#         a.append(weight_one[i])
# print(a)

# 全组合
# def per(arr, start, num, res):
#     if num == 0:
#         h.append(deepcopy(res))
#         return
#     elif len(arr)-start < num:
#         return
#     else:
#         res.append(arr[start])
#         per(arr, start+1, num-1, res)
#         res.pop()
#         per(arr, start+1, num, res)
# global h
# h = []
# arr = a
# start = 0
# resul = []
# for i in range(1, len(arr)+1):
#     per(arr, 0, i, resul)
# # print(h)
#
# h_one = []
# for i in h:
#     n_one = 0
#     for m in i:
#         n_one += int(m)
#     h_one.append(n_one)
# h_one.append(0)
# result = set(h_one)
# print(len(result))


# 网上的写法
# while True:
#     try:
#         n = int(input())
#         m = input().split(" ")
#         x = input().split(" ")
#         # mx为所有砝码，比如示例mx为[1, 1, 2]
#         mx, l = [], {0}
#         for i in range(n):
#             mx.extend([int(m[i])] * int(x[i]))
#         for i in mx:
#             # 每次加一块砝码，使用union(并集)得到新去重的组合，如果不使用union则稍微麻烦一点，需要考虑循环中改变set
#             l = l.union({i+j for j in l})
#         print(len(l))
#     except:
#         break

# 全组合做递归的思路，比如在一个长度为n的字符串中选择m个字符，对于第一个字符有两种选择，选或者不选。
# a)选择长度为n的字符串中的第一个字符，那么要在其余的长度n-1的字符串中选择m-1个字符
# b)第二是不选择长度为n的字符串中的第一个字符，那么要在其余的长度n-1的字符串中选择m个字符
# 结束条件
# a)已经找到了m个字符，即当m==0时结束；b)当剩余字符串的长度小于m时，结束递归。
# from copy import deepcopy
# # global定义全局变量，不论该变量，在哪里发生了变化，值都会发生变化，局部变量只会在相应的函数内发生变化
# h = []
# def per(arr, start, num, res):
#     global h
#     if num == 0:
#         h.append(deepcopy(res))
#         return
#     elif len(arr) - start < num:
#         return
#     else:
#         # 这个就是选择长度为n的字符串中的第一个字符
#         res.append(arr[start])
#         # 然后就在剩余长度n-1的字符串中选择m-1个字符
#         per(arr, start+1, num-1, res)
#         # 这个删除末尾一个元素的代码，理解可以根据arr = ['a','b','c']，num=2的情况来理解，是产生'ac'的情况，上面是产生'ab'的情况
#         res.pop()
#         per(arr, start+1, num, res)
#
# arr = ['a', 'b', 'c']
# res = []
# for i in range(1, len(arr)+1):
#     per(arr, 0, i, res)
# print(h)


# 全排列
import copy
# 用一个全局变量记录每次递归得到的结果
# All_permutation = []

# 递归函数,arr表示当前的排列,如[a,b,c],next表示当前排列中前next个数已经确定,需要从next+1的位置开始交换
# 注意列表下标从0开始,next表示的是下标
# 如next=1时,说明第一个数确定为1,然后从第二个数开始直到列表的结尾,每个数都要与第二个数进行一次交换
# def allPermutation(arr, next):
#     # 当next=len(arr)-1时,此时只剩下一个数要排列,直接就是结果
#     if next == len(arr) - 1:
#         global All_permutation
#         All_permutation.append(arr)
#     else:
#         # 从第next+1个数开始,每个数与第next+1的数进行一次交换(包括自己)
#         for i in range(next, len(arr)):
#             # 深拷贝,避免影响到原来的排列情况
#             update_permutation = copy.deepcopy(arr)
#             # 确定每次排列时的第一个数
#             update_permutation[i], update_permutation[next] = update_permutation[next], update_permutation[i]
#             allPermutation(update_permutation, next + 1)
#
#
# allPermutation(['a', 'b', 'c'], 0)
# print(All_permutation)

# 第三十八题
# n_one = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine',
#      '10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen'
#     ,'18':'eighteen', '19':'nineteen'}
# n_two = {'20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}
# a = []
#
# def test(num):
#     global a
#     if len(num) <= 3:
#         a.append(num)
#     else:
#         num_one = num[-3:]
#         a.append(num_one)
#         num = num[:-3]
#         test(num)
#
# def p(b):
#     rs = ''
#     if len(b) == 3:
#         for i in range(3):
#             if i == 0:
#                 if b[i] == '0':
#                     continue
#                 else:
#                     if b[1] == b[2] == '0':
#                         c = n_one[b[i]] + ' hundred '
#                     else:
#                         c = n_one[b[i]] + ' hundred and '
#                     rs += c
#             elif i == 1:
#                 if b[1] == '0':
#                     continue
#                 elif b[1] == '1':
#                     d = '1' + b[2]
#                     rs += n_one[d]
#                     break
#                 else:
#                     d = b[i] + '0'
#                     rs += n_two[d] + ' '
#             else:
#                 if b[2] == '0':
#                     continue
#                 else:
#                     rs += n_one[b[i]]
#     elif len(b) == 2:
#         if b[0] == '1':
#             c = '1' + b[1]
#             rs += n_one[c]
#         else:
#             c = b[0] + '0'
#             if b[1] == '0':
#                 rs += n_two[c]
#             else:
#                 rs += n_two[c] + ' ' + n_one[b[1]]
#     else:
#         rs += n_one[b[0]]
#     return rs
#
#
# m = input()
# test(m)
# b = []
# for i in range(len(a)):
#     b.append(p(a[i]))
# c = ''
# if len(b) == 3:
#     c = b[-1] + ' million ' + b[-2] + ' thousand ' + b[-3]
# elif len(b) == 2:
#     c = b[-1] + ' thousand ' + b[-2]
# else:
#     c = b[-1]
#
# print(c)

# 第三十九题
# while True:
#     try:
#         str1 = input()
#         k = int(input())
#         print(str1[:k])
#     except: break

# 第四十题
# def jy(a):
#     b = set(a)
#     c = []
#     for i in b:
#         c.append(a.count(i))
#     d = sorted(c)
#     e = 0
#     f = 26
#     h = d[0]
#     g = []
#     for i in range(1, len(d)):
#         g.append(d[-i])
#     g.append(h)
#
#     for i in range(len(g)):
#         e += g[i] * f
#         f -= 1
#     print(e)
#
# while True:
#     try:
#         n = int(input())
#         for i in range(n):
#             m = input()
#             jy(m)
#     except:
#         break


# 第四十一题
# while True:
#     try:
# map(function， *iterables)创建一个迭代器，作用是将传入的函数变量作用到第二个变量中的每个元素中，并将结果组成新的列表
# 换句话说就是第二个变量中的所有数据，都作为参数执行一遍function函数，然后再将结果组成新的列表
#         m, n = list(map(int, input().split()))
#         maze = []
#         for _ in range(m):
#             maze.append(list(map(int, input().split())))
#
#         def walk(i, j, pos=[(0, 0)]):
#             # 比如说第一种示例中的(2,0)参数，进来先条件判断可以走的方向，它可以走向右、向下和向上；
#             # 然后再通过第二个if条件语句来判断是否已经存在了，如果存在了就可以避免重复走，所以只能走向下或者向右，向上的
#             # 坐标已经保存在pos中了，向左和向上都是后退路径，所以都是j-1或者i-1
#             if j + 1 < n and maze[i][j + 1] == 0:  # 向右
#                 if (i, j + 1) not in pos:
#                     walk(i, j + 1, pos + [(i, j + 1)])
#             if j - 1 >= 0 and maze[i][j - 1] == 0:  # 向左
#                 if (i, j - 1) not in pos:
#                     walk(i, j - 1, pos + [(i, j - 1)])
#             if i - 1 >= 0 and maze[i - 1][j] == 0:  # 向上
#                 if (i - 1, j) not in pos:
#                     walk(i - 1, j, pos + [(i - 1, j)])
#             if i + 1 < m and maze[i + 1][j] == 0:  # 向下
#                 if (i + 1, j) not in pos:
#                     walk(i + 1, j, pos + [(i + 1, j)])
#
#             if (i, j) == (m - 1, n - 1):           # 到达出口
#                 for p in pos:
#                     print('(' + str(p[0]) + ',' + str(p[1]) + ')')
#
#         walk(0, 0)
#     except:
#         break


# 第四十二题






















