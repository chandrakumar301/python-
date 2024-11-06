# def unique(arr,n,k):
#     if n==0:
#         return "no elements"
#     j=0
#     j=arr[k-1]
#     arr.pop(arr[k-1])
#     if j not in arr:
#         return j
#         arr.append(j)
#       unique(arr,n-1,k+1)
def unique(arr,ele,n,k)
        ele.append(val)
    arr.append(val)
    return unique(arr,ele,n-1,k)
arr=[1,2,2,2,2,23,3,3,34,4,4,4,4,4,4,4]
n=len(arr)
k=0
print(unique(arr,[],n,k))