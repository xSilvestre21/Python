def countApplesAndOranges(s, t, a, b, apples, oranges):
    interval = [s, t]
    add = 0
    counter_apple = 0
    counter_orange = 0 
    for i in apples:
        add = i + a
        if add >= interval[0] and add <= interval[1]:
            counter_apple = counter_apple + 1
    for i in oranges:
        add = i + b
        if add >= interval[0] and add <= interval[1]:
            counter_orange = counter_orange + 1
    print(counter_apple)
    print(counter_orange)