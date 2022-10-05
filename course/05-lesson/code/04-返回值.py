#  返回值，返回值就是函数执行以后返回的结果
# 可以通过return来制定函数的返回值
# 可以直接使用函数的返回值，也可以通过一个变量来接受函数的返回值
def sum(*nums):
	result=0
	for i in nums:
		result  +=i
	print(result)
# sum(234,234,467)

# return  后面跟什么值，函数就会返回什么值,可以跟任意对象

def fn ( ):
	# return 'hello'
	# return{'a':1,'b':2}
	def fn2():
		print('hello')
	return fn2
e=fn ()
e()
# print(fn())


# 如果仅仅写一个return或者不写return，相当于return  None
def fn2():
	return
# r =fn2()
# print(r)

# def fn3():
# 	print('hello')
# 	return 4
# 	print('abc')
# r =fn3()
# print(r)

# def sum(*nums):
# 	result=0
# 	for i in nums:
# 		result +=i
# 	# print(result)
# 	return result
# r = sum(12,13,14)
# print(r)

# fn5 和 fn5()的区别
# def fn5( ):
# 	return 10

# print(fn5)#fn5是函数对象，打印fn5实际是在打印函数对象  <function fn5 at 0x0000020E99A3F910>
# print(fn5())#fn5()是在调用函数，打印fn5()实际上是在打印fn5()函数的返回值