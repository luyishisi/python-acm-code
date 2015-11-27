L=[a,b,c]
L.sort()
if L[0] + L[1] <= L[2]:
    print('W')
else:
    if L[0]*L[0] + L[1]*L[1] == L[2]*L[2]:
        print('Z')
    elif L[0]*L[0] + L[1]*L[1] > L[2]*L[2]:
        print('R')
    else:
        print('D')
