#remove duplicates elements in list
def duplicate(a,n):
    if n==0:
        return a
    temp=0
    k=0
    for j in a:
        for i in range(1,n):
            if j==a[i]:
                temp=a[i]
    return temp
a=[1,2,3,3,4,4,3,4,4]
n=len(a)
print(duplicate(a,n))
