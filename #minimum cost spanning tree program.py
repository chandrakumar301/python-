def max(arr,k):
    if k==0  :
        return "no elements"
    for j in range(0,k):
        if arr[j]>arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
    max(arr,k-1)
    return arr
arr=[10,2,3,5,7,8,1]
n=len(arr)
print(max(arr,n-1))
