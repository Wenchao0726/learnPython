# 不定长参数
# 定义一个函数，可以求任意数字的和
# def sum (*a):
# 	result= 0
# 	for n in a:
# 		result +=n 
# 		print('result=',result)
# sum(2,9,6,)


# sum(123,345,567)
# 在定义函数时，可以在形参前面加上一个*，这样这个形参将会获取到所有的实参
# 它会将所有的实参保存到一个元组中
# a,b,*c=(1,2,4,5,6,7)

# *a会接受所有的位置实参，并且会将这些实参同意保存到一个元组中（装包）
# def  fn  (*a):
# 	print('a=',a,type(a))
# fn (1,3,5,6)


# 带星号的形参只能有一个
# 带星号的形参，可以和其他参数配合使用
# def fn(a,b,*c):
# 	print('a=',a)
# 	print('b=',b)
# 	print('c=',c)
# fn(1,2,4,5,6)
	

# 可变参数不是必须写在最后，但是注意，带*的参数后所有参数，必须以关键字的形式传递，
# 第一个参数给a，剩下的位置参数给b的元组，c必须使用关键字参数
# def fn(a,*b,c):
# 	print('a=',a)
# 	print('b=',b)
# 	print('c=',c)
# fn(1,2,4,5,c=6)

# 所有位置参数都给a,b和c必须使用关键字参数
# def fn2(*a,b,c):
# 	print('a=',a)
# 	print('b=',b)
# 	print('c=',c)
# fn2(1,2,3,b=4,c=5)

#如果在形参的开头直接写一个*，则要求我们所有的参数必须以关键字参数形式传递
# def fn(*,a,b,c):
# 	print('a=',a)
# 	print('b=',b)
# 	print('c=',c)
# fn(a=2,b=3,c=4)

#*形参只能接受位置参数
# def fn3(*a):
# 	print('a=',a)
# fn3(b=1,c=2)

# **形参可以接受其他关键字参数,会将这些参数同意保存一个字典中
	# 字典的key就是参数的名字，字典的value就是参数的值
# **形参只能有一个，并且必须写在所有参数最后
# def fn3(b,c,**a):
# 	print('a=',a)
# 	print('c=',c)
# 	print('b=',b)
# fn3(b=1,c=3,d=4)


# 参数的解包
def fn(a,b,c):
	print('a=',a)
	print('b=',b)
	print('c=',c)
# 创建一个元组
t=(12,23,34)
# 传递实参时，也可以在序列类型的参数前添加星号，这样他会自动将序列中的元素以此作为参数传递
# 这里要求序列中的元素的个数必须和形参的个数一致
# fn(*t)

# 创建一个字典
d ={'a':12,'b':13,'c':14}
# 通过**来对一个字典进行解包操作
fn(**d)







