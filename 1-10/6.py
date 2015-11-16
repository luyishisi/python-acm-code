'''
输出100以内的所有素数，素数之间以一个空格区分
'''
print ''.join(map(str,filter(lambda x:not[x%i for i in range(2,x/2+1) if x%i == 0],range(2,101))))
'''
这个解析略难
lambda x:not[x%i for i in range(2,x/2+1) if x%i == 0]  只要x遍历所有的数，就能返回所有的素数了，因此想到了filter()函数

filter(lambda x:not[x%i for i in range(2,x/2+1) if x%i == 0],range(2,101))

此时还不满足格式要求

用map(str, [])，再用 ' '.join()一个，最终就是答案的形式了
'''
