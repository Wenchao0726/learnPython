# 遍历字典
# keys( )该方法会返回字典所有的key
d = {'name':'孙悟空','age':18,'address':'花果山'}

# 通过遍历keys()来获取所有的键
# n =1
# for k in d.keys():
	
# 	print(f'{n}',k,d[k])
# 	n =n+1

# print(d.keys())

# values( )
# 该方法会返回一个序列，序列中保存字典的所有值
# for v in d.values( ):
# 	print(v)

# items()
# 该方法会返回字典中所有的项
# 他会返回一个序列，序列中包含双值子序列
# 双值分别是，字典中的key和value
# print(d.items())
for k ,v, in d.items():
	print(k,'=',v)