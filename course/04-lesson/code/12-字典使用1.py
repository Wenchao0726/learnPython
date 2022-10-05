# 创建字典
# 使用{ }
# 语法:{k1:v1,k2:v2,k3:v3}

# 使用dict ()函数来创建字典
#，每一个参数都是一个键值对，参数名就是键，参数就是值（这种创建的字典，key都是字符串）
d = dict(name='孙悟空',age=18,gender='男')

# 也可以将一个包含有双值序列转换位为子序列
# 双值序列，序列中只有两个值，[2,3]('a','b'),'ab'
# 子序列，如果序列中的元素也是序列，那么我们就称这个元素为子序列
# [(1,3),(2,4)]
# d = dict([('name','孙悟空'),('age',18),('address','花果山')])

# len( )获取字典中键值对个数
# print(len(d))

# in 检查字典中是否包含指定的键
# not in 检查字典中是否不包含指定的键
# print('hello' in d)

# 获取字典中的值，根据键来获取值
# 语法：d[key]
# print(d['name'])

# n='name'
# print(d[n])

# 通过[ ]来获取值时，如果该键不存在，会抛出异常，keyerror
# get(key)该方法用来根据键来获取字典中的值，
# 	如果获取的键在字典中不存在，会返回none
# 	也可以指定一个默认只返回，作为第二个参数，这样获取不到值时，将会返回默认值
# print(d.get('name'))
# print(d.get('hello','默认值'))


# 修改字典
# d[key]=value  如果key存在则覆盖，不存在则添加
# d['name']='sunwukong'#修改字典的key- value
# d['address']='花果山'#向字典中添加key-value
# print(d)

# setdefault(key[ ,default])可以用来向字典中添加key-value
# 	如果key已经存在于字典中，则返回key的值，不会对字典做任何操作
# 	如果不存在，则向字典中添加这个key的值，并设置value
# result= d.setdefault('name','猪八戒')
# result = d.setdefault('hello','猪八戒')
# print('result=',result)
# print(d)

# update([other])
# 将其他的字典中的key-value添加当前字典中
# 如果有重复的key，则后边的会替换到当前
# d={'a':1,'b':2,'c':3}
# d2={'d':4,'e':5,'f':6}
# d.update(d2)
# print(d)
# # 删除，可以使用del来删除字典中的key-value
# del d['a']
# del d ['b']
# print(d)

# popitem()
# 随机删除字典中的一个键值对，一般会删除最后一个键值对,删除的键值对会作为返回值返回
# d.popitem()
# result = d.popitem()

# pop('key','返回值')
# 根据key删除字典中的key-value
# 会将值返回，如果删除不存在的值，会抛出异常，如果指定默认值，不会报错。
# result=d.pop('d')

# clear()用来清空字典当
# d.clear()

# cope()
# 该方法用于字典潜复制
# 复制以后的对象是独立的，修改一个不会影响另一个
# 浅复制只是简单复制对象的内部的值，如果值也是一个可变对象，这个可变对象不会对被复制
d={'a':1,'b':2,'c':3}
d2=d.copy()

print(d,id(d))
print(d2,id(d2))