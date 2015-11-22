'''
描述:
现在来练习一下发现爱的能力，给你一个字符串a,
如果其中包含"LOVE"（love不区分大小写)则输出LOVE，
否则输出SINGLE。
'''
if a.lower().find('love') == -1:
    print('SINGLE')
else:
    print('LOVE')
