'''
描述:
把一个偶数拆成两个不同素数的和，有几种拆法呢？
现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
计算将该数拆成两个不同的素数之和的方法数，并输出。
如n=10，可以拆成3+7，只有这一种方法，因此输出1.
'''
l=filter(lambda x:all(map(lambda p:x%p!=0,range(2,x))),range(2,n))
ll=filter(lambda x:l.count(n-x)>0 and x!=n-x,l)
print len(ll)/2
