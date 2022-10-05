# break
# break可以用来立即退出循环语句（包括else）
# continue
# continue可以用来跳过当次循环
# break和continue都只是对他最近的循环起作用

# 创建一个5次循环
i = 0
while i < 5:
	if i ==3:
		break
	print(i)
	i +=1
else:
	print('循环结束')

# i = 0
# while i < 5:
# 	i += 1
# 	if i ==3:
# 		continue
# 	print(i)
# else:
	# print('循环结束')

# i = 0
# if i < 5:
# 	pass