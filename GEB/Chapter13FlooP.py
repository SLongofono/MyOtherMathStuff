# Valid FlooP programs:
# A function with a finite number of inputs
# They can contain the following symbols and terms
#    if, return, break, =, ==, +, <
# They can also contain any other valid FlooP or BlooP program
# There must always be a value returned and it must always be an integer
# Parentheses and colons are allowed for Python's formatting
# + can be used for arithmetic addition
# < can be used for arithmetic less-than
# * can be used for arithmetic multiplication
# Numeric constants are allowed
# The only variables allow are integers assigned to and taken from the Cell dictionary
# The Cell dictionary must be indexed by integers
# A while loop is allowed of the form 'while True:'


# Create an "infinite list of zeroes" to work with

from collections import defaultdict

def zero():
    return 0

class Cell:

    def __init__(self):
        self.CELLS = defaultdict(zero)
        
    def __getitem__(self,n):
        return self.CELLS[n]
    
    def __setitem__(self,n,val):
        if not type(n) == int:
            raise Exception("Cell can be indexed only by integers")
        if not type(val) == int:
            raise Exception("Cell can contain only integers")
        self.CELLS[n] = val


from Chapter13BlooP import MINUS,POWER,DIVIDE,REMAINDER,ROOT

        
def FACTORIAL(N):
    cell = Cell()

    cell[0] = 1
    cell[1] = 1
    
    while True:
        if N < cell[0]:
            return cell[1]
        
        cell[1] = cell[0]*cell[1] # <- performs the operation at a given level of "recusion"
        cell[0] = 1+cell[0]       # <- essentially tracking the level of "recusion"
        

def TWO_THREE_CODE(M,N):
    return POWER(2,M)*POWER(3,N)

# Not a valid FlooP program
# We can Godel number each Ackerman input as 2**M * 3**N
def A(M,N):
    print(f"A({M},{N}) = cell[{2**M*3**N}] = {A_clean(M,N)}")
    if M == 0:
        return N+1
    
    if N == 0:
        return A(M-1,1)
    
    return A(M-1,A(M,N-1))

# Ackerman function without printing anything
def A_clean(M,N):
    if M == 0:
        return N+1
    if N == 0:
        return A_clean(M-1,1)
    return A_clean(M-1,A_clean(M,N-1))

def A_expand(M,N,steps):
    if steps == 0:
        return f"fA({M},{N})"
    
    
        
       
def ACKERMAN(M,N):
    cell = Cell()
    
    cell[0] = TWO_THREE_CODE(M,N) # our position counter
    cell[1] = 1 # corresponds to ACKERMAN(0,0)
    cell[2] = 2 # corresponds to ACKERMAN(1,0)
    cell[3] = 2 # corresponds to ACKERMAN(0,1)
    
    



if __name__ == '__main__':
    
#    print(f"MINUS(56,27) = {MINUS(56,27)}")
#    print(FACTORIAL(5))
#    print(POWER(3,4))
    print()
    A(2,4)