import math
import random

# step 1

def annie_gcd(a, b):
    num = max([a, b])
    den = min([a, b])

    rem = num % den

    while rem != 0:
        num = den
        den = rem
        rem = num % den    
    
    return den

def annie_lcm(a, b):
    return int(a * b / annie_gcd(a, b))

def compare(a, b):
    return (annie_gcd(a, b) == math.gcd(a, b)) \
        and (annie_lcm(a, b) == math.lcm(a, b))

def confirm(n):
    count = 0
    for i in range(n):
        a = random.choice([i for i in range(1, 20001)]) 
        b = random.choice([i for i in range(100, 200)])
        if compare(a, b) == False:
            count = count + 1
    return count

confirm(10_000)

