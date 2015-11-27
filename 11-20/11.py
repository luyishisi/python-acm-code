'''
描述:
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
'''
num = 1
count = 0
for x in L:
    num = num * x
    while (num/10)*10 == num:
        num = num/10
        count = count + 1
print count
