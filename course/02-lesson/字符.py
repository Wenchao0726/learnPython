# 显示系统的欢迎信息
print('-'*30,'欢迎使用员工管理系统','-'*30)
# 创建列表
employers=['孙悟空\t20\t男\t花果山','猪八戒\t23\t男\t高老庄']
# 显示用户的选项
while True:
	print('请选择要做的操作：')
	print('\t1.查询员工')
	print('\t2.添加员工')
	print('\t3.删除员工')
	print('\t4.退出系统')
	user_chose= input('请选择你的操作[1-4]：')
	print('-'*80)
	if user_chose == '1':
		# 查询员工
		print('\t序号\t姓名\t年龄\t性别\t住址')
		# 创建变量
		n = 1
		for employer in employers :
			print(f'\t{n}\t{employer}')
			n +=1
		print('-'*80)
	elif user_chose == '2':
		# 添加员工
		# 获取添加员工信息
		employer_name = input('请输入姓名：')
		employer_age = input ('请输入年龄：')
		employer_gender = input('请输入性别：')
		employer_address = input ('请输入住址：')
		employer= f'\t{employer_name}\t{employer_age}\t{employer_gender}\t{employer_gender}'
		# 提示信息
		print('以下员工将打印系统中：')
		print('-'*80)
		print('\t姓名\t年龄\t性别\t住址')
		print(employer)
		print('-'*80)
		# 用户确认信息
		user_chose = input('确认请按Y/yes：')
		print('-'*80)
		if user_chose == 'y' or user_chose =='yes':
			employers.append(employer)
			print('添加成功')
		else:
			print('添加取消')
		pass
	elif user_chose == '3':
		# 删除员工
		del_num = int(input('请输入删除员工序号：'))
		if 0<del_num <= len(employers):
			del_i = del_num - 1
			print('以下员工将要删除：')
			print('-'*80)
			print('\t姓名\t年龄\t性别\t住址')
			print(employers[del_i])
			print('-'*80)
			# 用户确认信息
			user_chose = input('确认删除请按[y/yes]：')
			if user_chose == 'y' or user_chose =='yes':
				result = employers.pop(del_i)
				print('-'*80)
				print(result,'：删除成功')
				print('-'*80)
			else:
				print('删除取消')
				print('-'*80)
		pass
	elif user_chose == '4':
		print('谢谢使用，再见！')
		print('请按任意键退出！')
		break
		print('-'*80)
	else:
		print('输入错误，请重新输入')
		print('-'*80)
