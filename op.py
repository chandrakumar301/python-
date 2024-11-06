def counter(arr,n,val):
    count=0
    for i in range(n):
        if arr[i]==val:
            count=count+1
    return list([val,count])
arr=[1,1,1,1,1,2,2,2,2,3,3,3,3,3,2,4,4,4,4,4]
arr1=set(arr)
n=len(arr)
n1=len(arr1)
for j in arr1:
    k=counter(arr,n,j)
    print(max(k),end=" ")


