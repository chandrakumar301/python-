arr1=[4,1,1,7,4,1,4,4,1]
a=len(arr1)
arr1=sorted(arr1)
print(arr1)
count=0
k=0
for i in range(a-1):
    if k==a-1:
        break
    elif arr1[k]==arr1[k+1]:
        k=k+2
        count+=1
    else:
        k=k+1
print(count)
    

