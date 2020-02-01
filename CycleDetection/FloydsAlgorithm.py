# Find cycles produced by an interated fuction

def floyds_algorithm(func,x):
    slow = func(x)
    fast = func(func(x))
    # Run until both slow and fast are inside the
    # cycle
    while fast != slow:
        slow = func(slow)
        fast = func(func(fast))
    
    # Find the position where the cycle begins
    pos = 0
    slow = x
    while fast != slow:
        slow = func(slow)
        fast = func(fast)
        pos += 1
    
    # Find the length of the shortest cycle
    length = 1
    fast = f(slow)
    while fast != slow:
        fast = func(fast)
        length += 1
    
    ex = x
    for i in range(pos):
        ex = func(ex)
    
    cyc = []
    for i in range(length):
        cyc.append(ex)
        ex = func(ex)

    return pos,length,cyc

def iter_func(func,x,n):
    for i in range(n):
        x = func(x)
    return x


def f(n):
    D = {0:6, 1:6, 2:0, 3:1,
         4:4, 5:3, 6:3, 7:4,
         8:0}
    return D[n]

for start in range(8):
    print(f"Starting from {start}")
    print(floyds_algorithm(f,start))
    print()