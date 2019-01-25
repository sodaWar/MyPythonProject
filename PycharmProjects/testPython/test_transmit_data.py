# -*- coding:utf-8 -*-
a = 1

def changeInteger(a):
	a = a+1
	return a

print changeInteger(a)
print a

b = [1,2,3]

def changeList(b):
	b[1] = b[1] + 1
	return b

print changeList(b)
print b

#第一个函数传的变量是整数变量，函数对变量进行操作，但是不会影响原来的变量，因为
#对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（我们称此为值传递）
#第二个函数传的变量是表，函数对表进行操作后，原来的表会发生变化，因为
#对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递）