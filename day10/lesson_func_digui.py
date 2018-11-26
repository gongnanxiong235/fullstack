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