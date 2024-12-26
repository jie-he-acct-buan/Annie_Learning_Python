import math
import random


# step 1
# calculate gcd
def annie_gcd(a, b):
    num = max([a, b])
    den = min([a, b])

    rem = num % den

    while rem != 0:
        num = den
        den = rem
        rem = num % den    
    
    return den


# step 2
# lcm is a times b then devided by gcd
def annie_lcm(a, b):
    return int(a * b / annie_gcd(a, b))


# step 3
# compare whether annie's function with math library's 
def compare(a, b):
    return (annie_gcd(a, b) == math.gcd(a, b)) \
        and (annie_lcm(a, b) == math.lcm(a, b))


# step 4
# try to run annie_gcd and annie_lcm for n times,
# and confirm there are no differences from math library
def confirm(n):
    count = 0
    for i in range(n):
        a = random.choice([i for i in range(1, 20001)]) 
        b = random.choice([i for i in range(100, 200)])
        if compare(a, b) == False:
            count = count + 1
    return count


# step 5
# call confirm function
confirm(10_000)


# the end of the code