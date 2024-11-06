arr=[1,2,3,4,5,5,6,6]
n=len(arr)
sum=total=0
for i in arr:
    sum=sum+i
    total=sum/n
print(total,end=" ")
if n%2==0:
    mid=int(n/2)-1
    kid=float(arr[mid]+arr[mid+1])
    did=kid/2
else:
    k=int(n/2+1)
    did=arr[k]
print(did,end=" ")
temp=[]
arr1=set(arr)
for j in arr1:
    k=arr.count(j)
    temp.append([j,k])
d=dict(temp)
maxm=max(d.values())
for key in d.keys(): 
	if d[key] == maxm:
	    print(key)
        maxm=0
    
        