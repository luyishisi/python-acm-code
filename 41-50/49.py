'''
描述:
给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
a为32位整数，2 <= b <= 16
如a=3,b = 2, 则输出11
'''
d = '0123456789ABCEDFGHIJKLMNOPQRSTUVWXYZ'
def f(x,y):
    s = []
    while x>=y:
        s.append(x%y)
        x /=y
    s.append(x)
    return ''.join([d[c] for c in s[::-1]])

print (a<0 and '-' or '')+f(abs(a),b)
