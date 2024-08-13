'''checking prime or nit prime by using for loop in python by taking user input'''
n=int(input("Enter avalue "))
p=0
for i in range(2,n):
    if(n%i==0):
        p+=1
        print("not a prime number")
        break
    elif(p<=1):
        print("Number is prime number")
        break
   
    
