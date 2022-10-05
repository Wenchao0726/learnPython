#现实游戏界面
print('-'*20,'欢迎进入孙悟空大战白骨精','-'*20)
print('请你选择以下操作：')
print('\t1.孙悟空')
print('\t2.猪八戒')
print('-'*66)
player_game = input('请你选择英雄[1-2]：')
if player_game == '1' :
	print('恭喜你，你将选择孙悟空进行作战')
elif player_game == '2' :
	print('不好意思，由于你是非VIP玩家，将选择孙悟空作战')
else :
	print('选择错误，系统将自动分配孙悟空作战')
print('孙悟空生命值为2，攻击值为2')
# 显示身份信息
player_life = 2  
player_attack = 2
boss_life = 10
boss_attack = 10
while True :
	print('-'*66)
	print('请选择以下操作：')
	print('\t1.练级')
	print('\t2.打怪')
	print('\t3.逃跑')
	game_choose = input('请选择你的操作[1-3]：')
	if game_choose == '1':
		print('-'*66)
		player_life +=2
		player_attack +=2
		print(f'恭喜你升级了，你现在生命值为{player_life},攻击值为{player_attack}')
	elif game_choose == '2':
		print('-'*66)
		boss_life -= player_attack
		print(f'白骨精受到了{player_attack}点伤害')
		if boss_life <= 0:
			print('白骨精被孙悟空打死了')
			break
		player_life -=boss_attack
		print(f'->孙悟空<-受到了{boss_attack}点伤害')
		if player_life <= 0:
			print('孙悟空被白骨精打死了')
			break
	elif game_choose =='3':
		print('-'*66)
		print('孙悟空逃跑了')
		break
	else:
		print('-'*66)
		print('操作失误，请重新选择：')







