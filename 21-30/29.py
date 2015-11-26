'''
描述:
给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
若能，输出YES，否则输出NO。
'''
if (a+b > c and a+c > b and b+c > a and a-b < c and a-c < b and b-c < a):
    print ('YES')
else:
    print ('NO')
