'''
描述:
设有n个正整数,将他们连接成一排,组成一个最大的多位整数.
例如:3个整数13,312,343,连成的最大整数为:34331213
又如:4个整数7,13,4,246连接成的最大整数为7424613
现在给你一个正整数列表L，请你输出用这些正整数能够拼接成的最大整数。
note:测试数据已于2014年11月13日更新，以前通过的代码不一定能够再次通过。
'''
import functools

def cmps(s1, s2):
    if(int(s1+s2) == int(s2+s1)): return 0
    if(int(s1+s2) > int(s2+s1)): return 1
    if(int(s1+s2) < int(s2+s1)): return -1
                
print(''.join(sorted([str(x) for x in L], key = functools.cmp_to_key(cmps), reverse = 1)))
