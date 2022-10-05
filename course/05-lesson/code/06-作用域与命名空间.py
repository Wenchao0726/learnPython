# 作用域(scope)
# 作用域指的是变量生效的区域
b= 20
# def fn():
# 	a=10
# 	# print('函数内部','a=',a)
# 	print('函数内部','b=',b)
# fn ()
# print('函数外部','a=',a)
# print('函数外部','b= ',b)

# 在Python中共有两种作用域
# 全局作用域
# 	-全局作用域在程序执行时创建，在程序执行结束时销毁
# 	-所有函数以外的区域都是全局作用域
# 	-在全局作用域中定义的变量，都属于全局变量，全局变量可以在程序的任意位置被访问
# 函数作用域
# 	-函数作用域在函数调用时创建，在调用结束时销毁
# 	-函数每调用一次就会产生一个新的函数作用域
# 	-在函数作用域定义的变量，都是局部变量，他只能在函数内部被访问
# 	
#变量的查找
#	-当我们使用变量时，会有现在当前作用域中寻找该变量，如果有则使用 
# 		如果没有则继续去上一级作用域中寻找，如果有则使用
		# 如果依然没有则继续去上一级作用域中寻找，以此类推
		# 直到找到全局作用域，依然没有找到，则会抛出异常


# a=30
# def fn(a):
	
# 	def  fn2():
# 		print('fn2中','a=',a)
# 	fn2()
# fn(50)
# a=23
# def fn2():
# 	# 如果希望在函数内部修改全局变量，则需要使用global关键字，来声明变量
# 	global a#声明在函数内部的使用a是全局变量，此时再去修改a时，就是在修改全局的a
# 	a =35 #修改全局变量
# 	print('函数内部：','a=',a)
	
# fn2()
# print('函数外部：','a=',a)


# 命名空间（namespace）
# 命名空间指的是变量存储的位置，没一个变量都需要存储到指定的命名空间当中
# 每一个作用域都会有一个它对应的命名空间
# 全局命名空间用来保存全局变量，函数命名空间用来保存函数中的变量
# 命名空间实际上就是一个字典，是专门用来存储变量的字典

# locals( )用来获取当前作用域的命名空间
# 如果在全局作用域中调用locals()则获取全局命名空间，如果在函数作用域中调用locals()则获取函数命名空间。
# 返回的是一个字典
scope = locals( )#当前命名空间
print(type(scope))
# print(scope)
# print(scope['b'])
scope['c']=100#向一个字典中key-value就相当在全局创建了变量
# print(c)


def fn2():
	a = 13
	# scope=locals()#在函数内部调用locals()会获取到函数的命名空间
	# scope['f']=12#可以通过scope来操作函数的命名
	# print(scope)
	# globals( )函数可以用来在任意位置获取全局命名空间
	global_scope = globals()
	global_scope['c']=45
	print(global_scope)

fn2()
print(c)