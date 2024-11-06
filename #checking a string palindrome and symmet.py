#checking a string palindrome and symmetric or not
def fun(a,n):
    k=a[::-1]
    if a==k:
        return "palindrome"
    else:
        return "not palindrome"
def symm(a,n):
    j=a[:n]
    l=a[n:]
    if j==l:
        return "symmetric"
    else:
        return "not symmetric"
a="chacha"
n=len(a)//2
print(fun(a,n))
print(symm(a,n))
