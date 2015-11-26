'''
描述:
给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
'''
if(len(L)==len(set(L))):
    print("NO")
else:
    print("YES")

