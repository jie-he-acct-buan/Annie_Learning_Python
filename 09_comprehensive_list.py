# import the packages
import time
import datetime
import math
import turtle
import random

# q1
lst = []
for i in range(8):
    lst.append(i)
print(lst)

lst = [i for i in range(8)]
print(lst)


# q2
lst = []
for i in range(8):
    lst.append(str(i))
print(lst)

lst = [str(i) for i in range(8)]
print(lst)


# q3
lst = [random.randint(1, 13) for i in range(8)]
print(lst)


# Q4:
# Annie is playing a game. 
# Step 1: she tosses a coin. 
# If she gets a head, then she draw a poker card. 
# Otherwise she rolls two dice.

# Step2: The poker point or sum of the two dice points can be > = < 10
# Then what is the opportunity for the sum < 10?

def coin(n):
    head_or_tail = [random.randint(0, 1) for i in range(n)]
    return head_or_tail

def poker(n):
    card = [random.randint(1,13) for i in range(n)]
    return card

def dice(n):
    roll = [random.randint(1, 6) for i in range(n)]
    return roll




def prob(n):
    count = 0
    for i in range(n):
        if coin(1) == 0:
            game = poker(1)
        else:
            game = dice(2)

        if sum(game) >= 10:
            count = count + 1
    return count / n

start = datetime.datetime.now()
print(prob(1_000_000))   
end = datetime.datetime.now()
end - start


# Q5: how many 4-digit integer with the sum of the 4 digits = 26
numbers = []
count = 0
for i in range(1_000, 10_000):
    lst = [int(n) for n in str(i)]
    if sum(lst) == 26:
        count = count + 1
        numbers.append(i)
print(numbers)
print(count)


name = '.Annie_2014  '
lst = [2, 'double', 3, 'king', 'jarry', 88]
for l in lst:
    print("{}'s length is {}".format(l, len(str(l))))


annie_homework = 'Skateboarding made its Olympic debut at the Tokyo Games in 2021'

len(annie_homework.split(' '))



lst = ['a', 'n', 'n', 'i', 'e']

''.join(lst)