import re
from GEB.Chapter8TNT.StripSplit import strip_succ, strip_neg, split_add_mul, \
                                       split_logical, strip_qaunt

# Get variables
def get_vars(x):
    v = re.findall("[a-z]\'*",x)
    return set(v)

# Return all quantifications used
def get_quants(x):
    q = re.findall("[∀∃][a-z]\'*:",x)
    return set(q)

# Return all variables that appear in quantifications
def get_bound_vars(x):
    var = get_vars(x)
    quant = get_quants(x)
    bound = set([])
    for v in var:
        for q in quant:
            if v in q:
                bound.add(v)
                break
    return bound

# Return all variables that don't appear in quantifications
def get_free_vars(x):
    var = get_vars(x)
    bvar = get_bound_vars(x)
    return var-bvar
        


# Simplest parts
def is_var(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def is_num(x):
    x = strip_succ(x)
    if x == "0" or is_var(x):
        return True
    return False

def is_pure_num(x):
    x = strip_succ(x)
    if x == "0":
        return True
    return False



# Combined parts
# Variables and numbers are terms as are negations and arithmetic of them
def is_term(x):
    x = strip_neg(x)
    if is_var(x) or is_num(x):
        return True
    else:
        # Before splitting we strip out S from the left
        # This prevents an error is there is a chain of Ss outside the parentheses
        # Removing S cannot turn a non-term into a term so there is no risk here
        x = strip_succ(x)
        try:
            L,R = split_add_mul(x)
            return is_term(L) and is_term(R)
        except:
            return False

# Atoms are terms seperated by an equality
def is_atom(x):
    x = strip_neg(x)
    if "=" not in x:
        return False
    else:
        try:
            L,R = x.split("=",maxsplit=1)
            return is_term(L) and is_term(R)
        except:
            return False

def is_quantifier(x):
    x = strip_neg(x)
    if re.match("^[∀∃][a-z]\'*:$",x):
        return True
    return False

# Check if a string starts with a quantifier
def starts_quantifier(x):
    x = strip_neg(x)
    if re.match("^[∀∃][a-z]\'*:.*",x):
        return True
    return False

# Checks if a formula is a compound well-formed formula or is a valid part of
# such. Since valid parts are not technically well-formed we will check
# seperately for that.
def is_compound(x):
    x = strip_qaunt(x)
    if is_atom(x) or is_term(x) or is_quantifier(x):
        return False
    else:
        try:
            L,R = split_logical(x)
            # Remove negatives and quantifiers
            L = strip_neg(L)
            L = strip_qaunt(L)
            # Remove negatives and quantifiers
            R = strip_neg(R)
            R = strip_qaunt(R)
            if is_atom(L) or is_term(L) or is_quantifier(L):
                if is_atom(R) or is_term(R) or is_quantifier(R):
                    return True
                return is_compound(R)
            
            if is_atom(R) or is_term(R) or is_quantifier(R):
                if is_atom(L) or is_term(L) or is_quantifier(L):
                    return True
                return is_compound(L)
                    
            return is_compound(L) and is_compound(R)
        except:
            return False

def is_well_formed(x):
    # Only atoms and compounds of atoms are well-formed, smaller parts are still
    # valid but they are not specifically "well-formed"
    # Removing the leading quantifiers and negations can never change if a string
    # is well formed
    x = strip_qaunt(x)
    if is_compound(x) or is_atom(x):
        return True
    return False
        

def is_open(x):
    var = get_vars(x)
    quant = get_quants(x)
    for v in var:
        for q in quant:
            if v in q:
                return False
    return True

def is_closed(x):
    return not is_open(x)





if __name__ == '__main__':
    theorems = ["∀b:(d+Sb)=S(d+b)"]
    for i in theorems:
        print(f"is {i} well-formed? {is_well_formed(i)}")