# Valid BlooP programs:
# A function with a finite number of inputs
# They can contain the following symbols and term
#    if, return, break, =, ==, +, <
# They can also contain any other valid BlooP program
# Parentheses and colons are allowed for Python's formatting
# + can be used for arithmetic addition
# < can be used for arithmetic less-than
# * can be used for arithmetic multiplication
# The only variable allowed is a list named cell which can hold ony integers
# A for loop is allowed but its can only loop over either an input or over an
# element of cell, the 

def MINUS(M,N):
    cell = [0]
    
    if M < N:
        return cell[0]
    
    for _ in range(M):
        if cell[0]+N == M:
            return cell[0]
        
        cell[0] = cell[0]+1


def POWER(M,N):
    cell = [0]
    
    cell[0] = 1
    
    for _ in range(N):
        cell[0] = M*cell[0]
    
    return cell[0]


def TWO_TO_THE_THREE_TO_THE(N):
    cell = [0,0]
    
    cell[0] = POWER(3,N)
        
    cell[1] = POWER(2,cell[0])
        
    return cell[1]


def DIVIDE(M,N):
    cell = [0,0]
    if M < N:
        return cell[0]
    
    if N == 0:
        return cell[0]

    cell[0] = M
    cell[1] = 1
    
    for _ in range(M):
        cell[0] = MINUS(cell[0],N)
        
        if cell[0] < N:
            return cell[1]+1
        
        cell[1] = 1+cell[1]

    return cell[1]


def REMAINDER(M,N):
    cell = [0,0]
    if M < N:
        return cell[0]
    
    if N == 0:
        return cell[0]

    cell[0] = M
    cell[1] = 1
    
    for _ in range(M):
        
        cell[0] = MINUS(cell[0],N)
        
        if cell[0] < N:
            return cell[0]


def PRIME(N):
    out = 0
    cell = [0]
    if N == 0:
        return out
    
    cell[0] = 1
    for _ in range(MINUS(N,2)):
        cell[0] = 1+cell[0]
        if REMAINDER(N,cell[0]) == 0:
            return 0
    return 1

print(POWER(7,7))
print(TWO_TO_THE_THREE_TO_THE(3))
