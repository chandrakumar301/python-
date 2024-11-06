#zoho question
def Pyramid(n):
    if(n==1):
        return 0
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==0 or j==n-1):
                print(n,end=" ")
            else:
                print(" ",end=" ")
        print()
        i=i+2
        j=j+2
    return Pyramid(n-2)
arr=Pyramid(9)
print(arr)