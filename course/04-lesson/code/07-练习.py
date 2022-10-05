print('-'*30,'欢迎使用员工管理系统','-'*30)
# 创建一个列表,用来保存员工信息
employers = ['孙悟空\t18\t男\t花果山','猪八戒\t19\t男\t高老庄']
while True:
	# 先使用户选项
	print('请选择你要进行的操作：')
	print('\t1.查询员工')
	print('\t2.添加员工')
	print('\t3.删除员工')
	print('\t4.退出')
	user_choose = input('请选择（1-4）：')
	print('-'*80)
	if user_choose == '1':
		# 查询员工
		# 打印表头
		print('\t序号\t姓名\t年龄\t性别\t住址')
		# 创建一个变量，来表示员工序号
		n= 1
		# 显示员工信息
		for employer in employers:
			print(f'\t{n}\t{employer}')
			n   +=1
	elif user_choose == '2':
		# 添加员工
		# 获取要添加员工的信息，姓名，年龄，性别，住址
		employer_name = input('请输入员工的姓名：')
		employer_age = input('请输入员工的年龄：')
		employer_gender = input('请输入员工的性别')
		employer_address = input ('请输入员工的住址')
		# 创建员工信息
		# 将四个信息拼接一个字符串，然后插入到列表中
		employer = f'{employer_name}\t{employer_age}\t{employer_gender}\t{employer_address}'
		# 显示一个提示信息
		print('以下员工将被添加到系统中')
		print('-'*80)
		print('姓名\t年龄\t性别\t住址')
		print(employer)
		print('-'*80)
		user_confirm = input('是否确认该操作[Y/N]:')
		# 判断
		if user_confirm =='y' or user_confirm=='yes':
			employers_append(employer)
			print('添加成功！')
		else:
			print('添加取消！')
	elif user_choose == '3':
		# 删除员工，根据员工序号来删除员工
		# 获取要删除的员工的序号
		del_num = int(input('请输入删除员工序号：'))
		# 判断是否有效
		if 0 <del_num <= len(employers):
			del_i = del_num-1
			# 显示一个提示信息
			print('以下员工将被删除')
			print('-'*80)
			print('姓名\t年龄\t性别\t住址')
			print(f'\t{del_num}\t{employers[del_i]}')
			print('-'*80)
			user_confirm = input('该操作不可恢复，时候确认[Y/N]:')
			# 判断
			if user_confirm == 'y' or user_confirm=='yes':
				# 删除元素
				employers.pop(del_i)
				# 显示信息
				print('员工已被删除')
			else:
				print('操作取消')


		else:
			# 输入有误
			print('你的输入有误，请重新操作！')

	elif user_choose == '4':
	# 退出
		print('欢迎使用，再见')
		input('点击回车键退出')
		break
	else:
		print('你输入有误，请重新输入')

	# 打印分割线
	print('-'*80)