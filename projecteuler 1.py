def euler1(zahl):
    l = []
    l.extend(range(3,1000,3))
    b = []
    b.extend(range(5,1000,5))
    l.extend(b)
    l = list(set(l))
    print(sum(l))
euler1(1)
