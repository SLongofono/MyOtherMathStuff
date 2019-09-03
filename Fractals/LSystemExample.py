from LSystem import LSystem

def func1(S):
    if S == "A":
        return "AB"
    if S == "B":
        return "A"
    else:
        return S
    
def func2(S):
    if S == "A":
        return "AA"
    if S == "B":
        return "A[B]B"
    else:
        return S
    
def func3(S):
    if S == "|":
        return "|_|"
    if S == "_":
        return "___"
    else:
        return S

for i in LSystem("A",func1):
    print(i)
print()

for i in LSystem("B",func2):
    print(i)
print()

for i in LSystem("|",func3):
    print(i)
    print()
print()

