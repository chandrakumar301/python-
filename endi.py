def sum(a,n):
    for i in range(0,n,1):
        rightsum=leftsum=sum=sum1=0
        rightsum=a[i:]
        leftsum=a[:i]
        print(rightsum,leftsum)
    
        
a=[6,7,7]
n=len(a)
sum(a,n)