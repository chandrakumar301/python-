import math

def is_prime(N):
    if N <= 1:
        return "No"
    if N == 2 or N == 3:
        return "Yes"
    if N % 2 == 0 or N % 3 == 0:
        return "No"
    
    # Check divisors from 5 to sqrt(N)
    limit = int(math.sqrt(N)) + 1
    for i in range(5, limit, 6):
        if N % i == 0 or N % (i + 2) == 0:
            return "No"
    
    return "Yes"

# Input
N = int(input())

# Output
print(is_prime(N))
