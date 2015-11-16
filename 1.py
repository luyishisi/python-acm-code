a,b = et.split(':'),st.split(':')
c,d = int(a[0]*3600) + int(a[1]*60) +int(a[2]),int(b[0]*3600) + int(b[1]*60) +int(b[2])
print c-d
