# finding a prime numbers in a given list using while loop in python
num=[13,24,57,19,5,7]
i=0
k=0
#using while loop
while k<len(num):
    if (num[k]%2==0):
        print("Given number is not prime ",num[k])
        i+=1 
    elif(i<=2):
        print(" give number is prime number",num[k])
    k+=1
    
    