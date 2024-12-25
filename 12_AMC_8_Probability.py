import random
import math
import time

def dice(n):
    lst = []
    for i in range(n):
        r = random.randint(1, 6)
        lst.append(r)
    return lst


################################################################################
# question 1
# the faces of a fair 6-slided die are numbered from 1 to 6. 
# what is the probability that when it is rolled,
# a 2 is facing up?

def dice(m ) :
    count = 0
    for i in range(m):
        r = random.randint(1, 6)
        if r == 2:
            count += 1
    return count / m

dice(10_000_000)


################################################################################
# question 2
# suppose we flip four coins sumultaneously:
# a penny, a nickel, a dime, and a quarter.
# what is the probability that

# 2.1. they all come up heads?

def coin_head(m):
    count = 0
    for i in range(m):
        lst = []
        p = random.randint(0, 1) # let 0 denote head and 1 denote tail
        lst.append(p)
        n = random.randint(0, 1)
        lst.append(n)
        d = random.randint(0, 1)
        lst.append(d)
        q = random.randint(0, 1)
        lst.append(q)

        if lst == [0, 0, 0, 0]:
            count += 1 

    return count / m

coin_head(1_000_000)

# 2.2. at least 15 cents worth of coins come up head?
def coin_15_cents(m):
    count = 0
    for i in range(m):
        lst = []
        p = random.randint(0, 1) # let 1 denote head and 0 denote tail
        lst.append(p)
        n = random.randint(0, 1)
        lst.append(n)
        d = random.randint(0, 1)
        lst.append(d)
        q = random.randint(0, 1)
        lst.append(q)

        value = 1 * lst[0] + 5 * lst[1] + 10 * lst[2] + 25 * lst[3]
        if value >= 15:
            count += 1

    return count / m

coin_15_cents(1_000_000)


################################################################################
# question 3
# two fair 6-sided dice are rolled. 
# what is the probability that

# 3.1. "double" are rolled (the two dice show the same number)?









# hint
lst = ['2', '3']
set(lst)
len(set(lst))


lst = ['2', '2']
set(lst)
len(set(lst))


lst = ['a', 'b', 'c', 'b']
set(lst)
len(set(lst))


lst = ['annie', 'Annie', 'ANNIE', 'Annie']
set(lst)
len(set(lst))



# 3.2. the sum rolled is 9?






# 3.3. the sum rolled is greater than 3 but less than 7?




# 3.4. at least one of the dice shows a 1?




# hint:
lst = ['a', 'b', 'c']
'a' in lst
'd' in lst




################################################################################
# question 4
# a number is selected at random from 1 through 100 inclusive. 
# what is the probability that the number

# 4.1. is a perfect square?






# hint:
number = 99
number ** 0.5
round(number ** 0.5)


number = 100
number ** 0.5
round(number ** 0.5)
round(number ** 0.5) == (number ** 0.5)

# 4.2. is a nultiple of 3?



# 4.4. is a divisor of 50?








################################################################################
# question 5
# a box contains 4 white balls and 4 black balls.
# i drew them out of the box, one at a time.
# what is the probability that all of my draws alternate colors?


































def alter_color(m):
    count = 0
    for j in range(m):

        box = 4 * [0] + 4 * [1]
        draw = []

        for i in range(8):
            r = random.choice(box)
            draw.append(r)
            box.remove(r)

        if draw == 4 * [0, 1] or draw == 4 * [1, 0]:
            count += 1

    return count / m

alter_color(1_000_000)




################################################################################
# question 5
# a senate committee consists of 5 republicans, 6 democrats, and 2 independents.
# a subcommittee of 3 members is randomly chosen.
# what is the probability that thte subcommittee

# 5.1. consists of 3 republicans?





































def three_rep(m):
    count = 0
    cmt = 5 * ['r'] + 6 * ['d'] + 2 * ['i']

    for i in range(m):
        sub = random.sample(cmt, k=3)
        if sub == ['r', 'r', 'r']:
            count += 1

    return count / m

three_rep(1_000_000)

# 5.2. consists of 1 replublican, 1 democrat, and 1 independent?






def one_one_one(m):
    count = 0
    cmt = 5 * ['r'] + 6 * ['d'] + 2 * ['i']

    for i in range(m):
        sub = random.sample(cmt, k=3)
        if set(sub) == {'r', 'd', 'i'}:
            count += 1

    return count / m

one_one_one(1_000_000)


################################################################################
# question 6
# what is the probability that a random arrangement of the letters in the word
# "ILIKEMATH" will have both "I"s next to each other?
























def II(m):
    word = 'ILIKEMATH'
    length = len(word)

    count = 0
    for i in range(m):
        r = random.sample(word, length)
        ran_word = ''.join(r)

        if 'II' in ran_word:
            count += 1

    return count / m

II(1_000_000)




import random




def duck(m, n):
    count = 0
    for _ in range(n):
        lst = sorted([random.random() for i in range(m)])
        for i in range(m - 1):
            if lst[i + 1] - lst[i] >= 0.5:
                count += 1
        if lst[m - 1] - lst[0] <= 0.5:
            count += 1
    print('{:.2%}'.format(count / n))



duck(4, 1_000_000)


def expected_value(n):
    '''
    this function similates rolling a dice for n times,
    and calculate the average outcome (expected value)
    '''
    import random
    summ = 0
    for _ in range(n):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        summ = summ + dice
        avg_outcome = summ / n
    return avg_outcome

for n in [10, 100, 1_000, 10_000, 100_000, 1_000_000]:
    print('The average outcome of rolling a dice for {:,} times is {:.2f}'\
          .format(n, expected_value(n)))










# new question
lst = []
for i in range(10, 101, 1):
    d = i % 10
    t = i // 10
    if i % (d + t) == 0:
        lst.append(i)
print(lst)

