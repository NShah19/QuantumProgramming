import random

def grover(f, n):
    """
    Grover's problem:
    Input: a function f : {0, 1}^n → {0, 1}
    Output: 1 if there exists x ∈ {0, 1}^n such that f(x) = 1, and 0 otherwise
    Notation: {0, 1}^n is the set of bit strings of length n
    """
    # Iterate over all possible binary permuations of n bits
    # return 1 if f(x) = 1 is found
    # return 0 once all possible permutations have been exhausted
 
    max_int = '0b' + '1' * n
    for i in range(0, int(max_int, 2)+1):
       if (f(str(format(i, 'b').zfill(n))) == 1):  
           print(str(format(i, 'b').zfill(n)))
           return 1
    return 0 

def negative_test(x):
    return 0

def positive_test(x):
    return 1

def random_test(x):
    
 11f4e98be39541765acf35b146b318685fbb2dd8 


if __name__ == '__main__':
