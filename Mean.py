# Enter your code here. Read input from STDIN. Print output to STDOUT
l=5
b=4
for i in range(l-1):
    for j in range(b+1):
        if i==0 or i==b-1 or j==0 or j==b-1:
            print("*",end="")
    print()



5
