
def sum(a,n):
    x=0
    for i in range(0,n,1):
        rightsum=leftsum=sum=sum1=0
        rightsum=a[i+1:]
        leftsum=a[:i]
        for l in leftsum:
            if i==0:
                sum=0
            else:
                sum+=l
        for k in rightsum:
            if i==n-1:
                sum1=0
            else:
                sum1+=k
        if sum>sum1:
            x=sum-sum1
        else:
            x=sum1-sum
        print(x,end=" ")
a=[6,7,7]
n=len(a)
sum(a,n)







