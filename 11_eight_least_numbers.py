

a = 10 
b = 18 

lst = []
c = 1
count = 0
while count < 8:
    if (c % a == 0) and (c % b == 0):
        count = count + 1
        lst.append(c)
    c = c + 1






lst = [i for i in range(10)]
lst.remove(1)
lst_s = [i for i in range(1, 10, 1)]

for s in lst_s:
    for e in lst:
        for n in lst:
            for d in lst:
                for o in lst:
                    for r in lst:
                        for y in lst:
                            if \
                               \
        (len(set([s, e, n, d, o, r, y])) == 7) \
        & ((1000*s + 100*e + 10*n + d) + (1000 + 100*o + 10*r + e) \
            == (10000 + 1000*o + 100*n + 10*e + y)):
                                print(' ', s, e, n, d)
                                print('+', 1, o, r, e)
                                print('-----------')
                                print(1, o, n, e, y)


set([1, 2, 3, 3])