def simon(f, n):
    """
    Simon's problem:
    Input: a function f: {0,1}^n → {0,1}^n.
    Assumption: there exists s in {0,1}^n such that for all x,y: 
    [f(x) = f(y)] iff [(x+y) in {0^n, s}].
    Output: s.
    Notation:
    {0,1}^n is the set of bit strings of length n, 
    s is an unknown bit string of length n, 
    = is comparison of bit strings of length n, 
    + is pointwise addition mod 2 of bit strings of length n, 
    and 0^n is a bit string of length n with all 0.  
    """
    

if __name__ == '__main__':
