def euler5(zahl):
    c = 1
    last = 0
    for i in range(1,21):
        while(c % i != 0):
            c += last
        last = c
        print(" For %d we have %d" % (i, c))


euler5(1)
