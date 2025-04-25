def kangaroo(x1, v1, x2, v2): 
    k1_jumps = 0 
    k2_jumps = 0
    for _ in range(10000):
        if x1 == x2 and k1_jumps == k2_jumps:
            return "YES"
        x1 += v1
        k1_jumps += 1
        x2 += v2
        k2_jumps += 1
        print(x1, x2)
    else:
        return "NO"


print(kangaroo(0, 3, 4, 2))