# 集合
# 使用{ }来创建集合，
s={1,7,6,4,}
# s = {[1,2,3,4,5],[12,]}   TypeError: unhashable type: 'list'

# 使用通过set()来将序列和字典转换为集合
s = set([1,2,4,5,"a"])
s= set("hello")
s = set({'a':1,'b':2,'c':3})#使用set()将字典转换为集合时，只会包含字典中的键


#创建集合
s = {'a','b',2,3,5}
#使用in 和not in 来检查集合中的元素
# print('a' in s )

# 使用len()来获取集合中元素的数量
# print(len(s))

# add( )向集合中添加元素
s.add(10)

# update( ) 讲一个集合中的元素添加到当前集合中
s2 ={'hello'}
s.update(set('hello'))

# pop( ）随机删除一个集合元素
# s.pop()
# result = s.pop()
# print(result)

# remove(）删除集合中的指定元素
s.remove('o')

# clear()清空集合
# s.clear()

# copy()对集合的浅复制

print(s)

