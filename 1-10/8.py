'''
list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。
'''
length=len(L)
if length%2!=0:
    print L[length/2+1]
else:
    print (L[length/2+1]+L[length/2])/2.0
