# + 和 -

# +可以将两个列表拼接位一个列表
# my_list = [1,2,3] + [4,5,6]
# print(my_list)

# * 可以将列表重复指定次数
# my_list = [1,2,3] *5
# print(my_list)

# 创建一个列表
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精','沙和尚','沙和尚']

# in 和 not in
# in用来检查指定元素是否存在于列表中
# 		如果存在，返回True
# 		如果不存在，返回False
# not in 用来检查指定元素不存在列表中
		# 如果不在，返回true，否则返回false
# print('' in stus	)

# len() 获取列表中的元素的个数

# min()获取列表中的最小值
# max()获取列表中的最大值
arr = [1,5,77,44,33,334]
# print(min(arr))
# print(max(arr))

# 两个方法(method),方法和函数基本上是一样，只不过方法必须通过对象.方法()的形式，调用
# xxx.print( ) 方法实际上就是核对相关系紧密的函数
# s.index() 获取指定元素在列表中第一次出现的索引
# print(stus.index('沙和尚'))
# index()的第二个参数，表示查找起始位置，第三个参数，表示查找的结束位置
# print(stus.index('沙和尚',3,7))
# 如果要获取列表中没有的元素，会抛出异常
# print(stus.index('牛魔王'))   Traceback (most recent call last):

# s.count()
print(stus.count(''))




