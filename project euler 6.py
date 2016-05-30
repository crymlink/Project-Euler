def euler6(zahl):
    l = []
    l.extend(range(1,101))
    b = sum(l)**2
    c = 0
    for i in range(1,101):
        c += i**2
    f = b - c
    print(f)
euler6(1)
