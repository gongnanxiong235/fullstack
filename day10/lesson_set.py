# author:gongnanxiong
# date:2018/11/22


'''
set的两大用途：
1.去重，把列表转换成set之后自动去重
2.关系式
set的key都是可哈希的，也就是key不能是列表和字典
set是可变的，非可哈希的，所以set也不能作为dict的key
set是无顺序的，所以不能像list一样通过下标找到元素，只能通过遍历和iter的方式
set是无顺序的，所以set.pop()是随机删除一个值
'''

set_a=set([1,2,3])
set_b=set([1,2,3])
print(set_a==set_b)
set_b.add(4)
print(set_a<set_b)
set_a.update([4,5,6])
print(set_a)
print(set_a>set_b)

# set_a.remove('hello')# 如果remove的key不存在会报错

# 差级
print(set_a.difference(set_b))
print(set_a-set_b)

# 反向差级
set_b.add(7)
print(set_a.symmetric_difference(set_b))
print(set_a^set_b)

# 取并集
print(set_a.union(set_b))
print(set_a|set_b)

print("---------")
print(set_a)
print(set_b)
print(set_a-set_b)

# 取交集
print(set_a.intersection(set_b))
print(set_a & set_b)

