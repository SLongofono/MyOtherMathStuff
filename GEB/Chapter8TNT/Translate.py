import re
from Utils.StringManip import bracket_matching
from GEB.Chapter8TNT.Properties import get_vars
from GEB.Chapter8TNT.StripSplit import replace_var

def make_austere(s):
    """
    Convert a string of TNT to austere TNT by rewriting all variables
    """
    V = get_vars(s)
    a = "a"
    for v in V:
        # Don't replace variables that are already use "a" type variables
        if "a" in v:
            continue
        # Otherwise find the next usable "a" type variable and use it as replacement
        else:
            while a in V:
                a += "'"                
            s = replace_var(s,v,a)
            a += "'"
    return s



def translate(s):
    """
    Translate a statement of TNT to 'plain english'
    """
    
    # Translate universal and existential quantifiers in order left to right
    # What we say changes depending on what follows
    Q = re.search("[∀∃][a-z]\'*:",s)
    while Q != None:
        
        lo, hi = Q.span()
        inside = s[lo+1:hi-1]
        left = s[:lo]
        right = s[hi:]
        
        if Q.group()[0] == "∀":
            # Chains of univerals use "and"
            if right[0] == "∀":
                s = f"{left} for all {inside} and {right} "
            # Universal followed by existential just needs a space
            elif right[0] == "∃":
                s = f"{left} for all {inside} {right} "
            # If the next statement is a negation translate to "it is false that"
            elif right[0] == "~":
                s = f"{left} for all {inside}, it is false that {right[1:]} "
            # Otherwise just a comma
            else:
                s = f"{left} for all {inside}, {right} "
                
        if Q.group()[0] == "∃":
            # Existential followed by universal use "such that"
            if right[0] == "∀":
                s = f"{left} there exists {inside}, such that {right} "
            # Chains of existentials use "and"
            elif right[0] == "∃":
                s = f"{left} there exists {inside} and {right} "
            # If the next statement is a negation translate to "such that it is false that"
            elif right[0] == "~":
                s = f"{left} there exists {inside}, such that it is false that {right[1:]} "
            # Otherwise use "such that"
            else:
                s = f"{left} there exists {inside}, such that {right} " 
                
        Q = re.search("[∀∃][a-z]\'*:",s)
    
    # Translate natural numbers
    N = re.search("S+0",s)
    while N != None:
        lo, hi = N.span()
        num = s[lo:hi]
        ctr = 0
        while num[0] == "S":
            ctr += 1
            num = num[1:]
        
        left = s[:lo]
        right = s[hi:]
        s = f"{left}{ctr}{right} "
        N = re.search("S+0",s)
    
    # Translate addition natural number addition of variables
    N = re.search("S+[a-z]\'*",s)
    while N != None:
        lo, hi = N.span()
        num = s[lo:hi]
        ctr = 0
        while num[0] == "S":
            ctr += 1
            num = num[1:]
        left = s[:lo]
        right = s[hi:]
        s = f"{left}({num} + {ctr}){right}"
        N = re.search("S+[a-z]\'*",s)
        
    # Translate even more generalized additions that remain
    # Needs to use a bracket matching system to isolate correctly
    N = re.search("S+\(",s)
    while N != None:
        braks = bracket_matching(s,"(",")")
        span = N.span()
        for i in braks:
            if i[1] == span[1]-1:
                num, lo, hi = i
                break
            
        left = s[:lo]
        right = s[hi:]
        
        ctr = 0
        if left != "":
            while left[-1] == "S":
                ctr += 1
                left = left[:-1]
                if left == "":
                    break
                
        s = f"{left}({num} + {ctr}{right}"
        N = re.search("S+\(",s)
        
    # Simple translations
    symbol = ["~","+","⋅","=","⊃","∨","∧","<",">"]
    translation = [" it is false that ",
                   " + ", " ⋅ ",
                   " = ", " implies that ",
                   " or ", " and ", "[", "]"]
    
    for sym,t in zip(symbol,translation):
        s = s.replace(sym,t)
        
    # Fix various spacing issues
    while "  " in s:
        s = s.replace("  "," ")
    
    s = s.replace("( ","(")
    s = s.replace(" )",")")
    s = s.replace("[ ","[")
    s = s.replace(" ]","]")
        
    if s[0] == " ":
        s = s[1:]
    
    return s



# Hofstadter's arithmetization of TNT
def translate_arithmetic(s,reverse=False):
    """
    Convert a string of TNT to its arithmetic coding
    If the string uses variables that aren't in austere 
    """
    
    for letter in "bcdefghijklmnopqrstuvwxyz":
        if letter in s:
            raise Exception("Only austere TNT can be made arithmetic by this function")
    
    if reverse == True:
        
        D = {"666":"0", "123":"S", "111":"=", "112":"+",
             "236":"⋅", "362":"(", "323":")", "212":"<",
             "213":">", "312":"[", "313":"]", "262":"a", 
             "163":"'", "161":"∧", "616":"∨", "633":"⊃", 
             "223":"~", "333":"∃", "626":"∀", "636":":"}
        
        out = ""
        while s != 0:
            s,codon = divmod(s,1000)
            out = D[str(codon)]+out
        return out
        
    else:
        D = {"0":"666", "S":"123", "=":"111", "+":"112",
             "⋅":"236", "(":"362", ")":"323", "<":"212",
             ">":"213", "[":"312", "]":"313", "a":"262", 
             "'":"163", "∧":"161", "∨":"616", "⊃":"633", 
             "~":"223", "∃":"333", "∀":"626", ":":"636"}
        
        for sym,codon in D.items():
            s = s.replace(sym,codon)
        
        return int(s)





if __name__ == '__main__':
    # Quick tests
    strings = ["~S0=0","SSSa=a'",
               "∀a:<<a+0=0∧0+a'=0>∨a''⋅0=0>",
               "∀a:∃a':(a+Sa')=S(a+a')",
               "~∀a:∃a:<a=a'⊃0=1>",
               "∀a:~∃a'':<a=0∧1=a'>",]
    for s in strings:
        print(f"{s}\n{translate(s)}\n{translate_arithmetic(s)}\n")
