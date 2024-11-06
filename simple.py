def meanmedianmode(a,n):
    if n==0:
        return a
    y,l,k=0,0,0
    for i in a:
        k+=i
    l=k/n
    if n%2==0:
        h=n//2
        y=(a[h-1]+a[h])/2
    else:
        h=a[n/2]
    def mode(a,n):
        r=0
        for i in ranage(n):
            if a[i]==a[i+1]:
                r+=1
            return r,a[i]
    print(l,y,z)
a=[1,2,3,4,5,5,6,6]
n=len(a)
meanmedianmode(a,n)