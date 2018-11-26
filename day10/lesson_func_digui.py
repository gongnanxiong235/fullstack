'''
递归
'''
def dr(n):
    if n==1:return 1
    else:return n*dr(n-1)

print(dr(3))

'''
斐波那契数列
'''
def fibo(n):
    result = [0, 1]
    if n==1:
        return 0
    if n==1:
        return result
    else:
        for i in range(n-2):
            result.append(result[-1]+result[-2])
        return result

print(fibo(3))


map_a=map(int,['1','2','3','4'])
print(list(map_a))

# 元素只要包含None 0 ‘’ 都返回false 其余都返回True
print(all([1,None]))

#重写all方法
def all_copy(seq):
    for i in seq:
        if not i:
            return False
    return True

print(all_copy([1,1,2,3,0]))