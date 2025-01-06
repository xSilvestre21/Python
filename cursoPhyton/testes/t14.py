def kangaroo(x1, v1, x2, v2):
    d1 = 0
    d2 = 0
    while True:
        d1 = x1 + v1
        d2 = x2 + v2
        if d1 == d2:
            break
    print(d1)


print(kangaroo(1, 2, 3, 4))