def euler4(zahl):
    c = []
    for i in range(100,1000):
        for n in range(100,1000):
            b = i*n
            if str(b) == str(b)[::-1]:
                c.append(b)
    c = list(set(c))
    print(max(c))
euler4(1)
