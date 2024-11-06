def max(a,n):
    if n==0:
        return a
    for i in range(n-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    return a[n-1]
def max(a,n):
    if n==0:
        return a
    for i in range(n-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    return a[n-1]
n=int(input())
a=list(map(int,input().split()))
n=len(a)
print(max(a,n))
