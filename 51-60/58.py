'''
描述:
给你一个正整数list L, 如 L=[2,8,3,50], 求列表中所有数的最小公倍数(不用考虑溢出问题）。
如L=[3,5,10], 则输出30
'''
def f(x,y):
    x,y = min(x,y),max(x,y)
    for i in range(1,x+1):
        if (y*i)%x == 0:
            return y*i
print(reduce(f,L))
