# author:gongnanxiong
# date:2018/12/13

from itertools import combinations,product,permutations,combinations_with_replacement

# a=combinations(['A','B','C','D','E','F','G'],1)
# # for i in a:
# #     print(i)


# def combination(code):
#     result_list=[]
#     code=code.lower ()
#     for i in range ( len ( code ) ):
#         combins=[c for c in combinations ( range ( len ( code ) ), i )]
#
#         for j in combins:
#             code_old=[]
#             # print(j)
#             for y in code:
#                 # print('y:',y)
#                 code_old.append ( y )
#             for z in j:
#                 code_old[z]=code_old[z].upper ()
#             result_list.append ( "".join ( code_old ) )
#     result_list.append ( code.upper () )
#
#     return set ( result_list )
#
#
# a=combination ( code="abcdefg" )
# print(a)



for i in combinations_with_replacement([1,2,3,4],3):
    print(i)
    print('-------')
#
# a=list ( range ( 97, 123 ) ) + list ( range ( 65, 91 ) )
# b=[chr(x) for x in a]
#
#



# 多个序列的组合(在每组中选择一个进行排列)
# 也可以一个集合的所有排列，其中包含重复
for i in product(['1','2','3','4'],['a','b','c']):
    print(i)


print('-------')

y=0
for i in permutations(['1','2','3','4'],3):
    y+=1
    print(i)
print(y)






