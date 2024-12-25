import time
import math


# =========================================================================
# question 1: GCD and LCM
# =========================================================================
# Greeting
print('Hi, I am a robot that calculates math!')
print()
time.sleep(2)


print('''
First, I can calculate the Greatest Common Divisor 
and the Least Common Multiple of two whole numbers.''')
print()
time.sleep(2)


# tell the robot two numbers
a = int(input('Can you give me a whole number? '))
b = int(input('Can you give me another whole number? '))
print()
time.sleep(1)


# robot calculates GCD
gcd = math.gcd(a, b)
print('The greatest common divisor of {:,} and {:,} is {:,}.'.format(a, b, gcd))
print()
time.sleep(2)


# robot calculates LCM
lcm = math.lcm(a, b)
print('The least common multiple of {:,} and {:,} is {:,}.'.format(a, b, lcm))
print()
print()
time.sleep(5)

print('====================================================================')






# =========================================================================
# question 2: Area and Perimeter of circles
# =========================================================================
print('Second, I can calculate the Perimeter and the Area of a circle.')
print()
time.sleep(2)


radius = float(input('Can you give me the radius of a circle? '))
print()
time.sleep(2)


# ====================================================
# method 1 to print 2 digits
# perimeter = 2 * math.pi * radius
# perimeter = round(perimeter, 2)

# area = math.pi * radius ** 2
# area = round(area, 2)

# # robot tells the answer
# answer = '''If the circle's radius is {},
# the perimeter is {} 
# and the area is {}.'''
# print(answer.format(radius, perimeter, area))


# =====================================================
# method 2 to print 2 digits
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2


# robot tells the answer
answer = '''If the circle's radius is {:,},
the perimeter is {:,.2f} 
and the area is {:,.2f}.'''
print(answer.format(radius, perimeter, area))
print()
time.sleep(5)
print('====================================================================')





# =====================================================
# Calcu-Bot says Goodbye
# =====================================================
goodbye =  '''
Thank you for doing math with me.
I need to take a break and have some food.
We can do more math tomorrow.
Bye!
'''
print(goodbye)









