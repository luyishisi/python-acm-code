'''
描述:
给你两个正整数a,b,  输出它们公约数的个数。
'''
n = 0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        n+=1
print(n)
