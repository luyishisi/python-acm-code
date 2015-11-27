'''
描述:
给你一个字符串列表L，请用一行代码将列表所有元素拼接成一个字符串并输出。
如L=['abc','d','efg'], 则输出abcdefg。
'''
print ''.join([str(x) for x in L])

from_futere__import print_function
print(*L,sep='')

