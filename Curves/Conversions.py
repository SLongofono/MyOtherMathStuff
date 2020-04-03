def xy_to_complex(x,y):
    return [a+b*1j for a,b in zip(x,y)]

def xy_to_point(x,y):
    return [(a,b) for a,b in zip(x,y)]

def point_to_complex(P):
    return [a+b*1j for a,b in P]

def point_to_xy(P):
    return [p[0] for p in P], [p[1] for p in P]

def complex_to_xy(C):
    return [z.real for z in C], [z.imag for z in C]

def complex_to_point(C):
    return [(z.real,z.imag) for z in C]


if __name__ == '__main__':
    x = [1,2,3,4,5]
    y = [5,4,3,2,1]
    P = [(1,5),(2,4),(3,3),(4,2),(5,1)]
    C = [1+5j,2+4j,+3+3j,4+2j,5+1j]
    
    print(x,y)
    print(P)
    print(C)
    
    print(xy_to_complex(x,y) == C)
    print(xy_to_point(x,y) == P)
    print(point_to_complex(P) == C)
    print(point_to_xy(P) == (x,y))
    print(complex_to_xy(C) == (x,y))
    print(complex_to_point(C) == P)