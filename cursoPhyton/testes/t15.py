import math

def getTotalX(a, b):
    mmc = math.lcm(*a)
    mdc = math.gcd(*b)
    count = 0
    
    for i in range(mmc, mdc + 1, mmc):
        if mdc % i == 0:
            count += 1
    
    return count

print(getTotalX([2, 4], [16, 32, 96]))