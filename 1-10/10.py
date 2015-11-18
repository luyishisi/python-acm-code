 #给你两个正整数ab，输出他们的最小公倍数。
 for i in range(max(a,b),a*b+1):
     if i%a==0 and i%b==0:
         print(i)
         break

