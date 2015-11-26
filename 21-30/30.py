'''
描述:
马上国庆节了，用一个英文单词描述你此时此刻的心情。
//
你可以想象我看到这题时候内心几乎就是奔溃的。
我想直接。输出。。fack。

'''
#答案是 print("Happy")   但是答案区有个神一样的代码。。
V=''
code=[72,97,112,112,121]
for x in range(0,5):
    while x<=4:
        if code[x]>0:
            V+=chr(code[x])
        break
print V



