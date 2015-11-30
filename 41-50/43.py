'''
描述:
斐波那契数列为1,1,2,3,5,8...。数列从第三项起满足，该项的数是其前面两个数之和。
现在给你一个正整数n（n < 10000), 请你求出第n个斐波那契数取模20132013的值（斐波那契数列的编号从1开始）。
'''
a = 1;b = 1;c =1;
for i in range(n-2):
    c = a+b;
    a ,b =b,c
    if(b > 20132013):
        a %= 20132013
        b %= 20132013
print(c%20132013)
