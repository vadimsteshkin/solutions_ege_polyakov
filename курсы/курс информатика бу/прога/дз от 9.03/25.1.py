def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(200918,210801):
    k=d(i)
    if len(k)==4:
        print(i,*k)