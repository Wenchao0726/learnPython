# 模块，通过模块可以对Python进行扩展
# 引入一个time模块，来统计程序执行时间
from time import * 
# time()函数可以用来获取当前的时间，返回单位是秒
# 优化前：
#  		10000个数 3.3秒
# 第一次优化：
			# 10000个数  0.3 秒
			# 100000个数34,7 秒
# 第二次优化：
			# 100000个数0	.36


# 获取程序开始时间
begin = time ()
i = 2
while i < 10000:
	flag = True
	j = 2
	while j <= i **0.5:
		if i % j == 0 :
			flag = False
			# 一旦进入判断，证明i一定不是质数，此时内层循环没有继续执行的必要
			# 使用break 退出内层循环
			break
		j += 1
	if flag  :
		pass
		# print(i)
	i +=1

#获取程序结束时间
end = time()
print('执行程序所需时间：',end - begin ,'秒')

