'''
描述:
M个人围成一圈，每分钟相邻的两个人可以交换位置（只能有一对交换）。
现在给你一个正整数n(0 < n < 1000)，求使n个人的顺序颠倒(即每个人左边相邻的人换到右边，右边相邻的人换到左边）所需的最少时间（分钟数）。
如：n=4, 输出2.
'''
print( n/2*(n/2-1)+(n%2)*n/2)
#组合数学的公式，，不怎么懂
