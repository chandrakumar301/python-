def Selection(list,n):
    if n==0:
        return 
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if list[min]>list[j]:
                min=j
        list[i],list[min]=list[min],list[i]
        return list
list=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(list)
print(Selection(list,n))




