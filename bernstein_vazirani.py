import random
import numpy as np

def bernstein_vazirani(f, n):
    """
    The Bernstein-Vazirani problem:
    Input: a function f : {0, 1}^n → {0, 1}.
    Assumption: f(x) = a × x + b.
    Output: a, b.
    Notation: {0, 1}^n is the set of bit strings of length n, 
    a is an unknown bit string of length n, × is inner product mod 2, 
    + is addition mod 2, and b is an unknown single bit.  
    """
    # Determine value of b. Note: f(00 . . . 0) = b
    zero_arr = np.zeros(n, dtype=int)
    b_val = f(zero_arr) 

    # Create a mask for each position i from 0 to n-1 
    # Pass in each mask to f to determine value at a[i]
    a_val = np.zeros(n, dtype=int)
    for i in range(n):
        input = np.zeros(n)
        input[i] = 1
        # If b is 0, the returned value from f is the value at a[i]
        # Otherwise, it is ~f
        if b_val == 0:
            if f(input) == 1:
                a_val[i] = 1
        else:
            if f(input) == 0:
                a_val[i] = 1
    print('Predicted Values: ', a_val, b_val)
    return a_val, b_val
   
def create_func(n):
    # f(x) = a × x + b
    # Generate a random array of size n for a
    a_str = random.randint(0, (2**n) - 1)
    a = np.array(list(format(a_str, 'b').zfill(n)), dtype=int)
    # Generate a random value for b
    b = random.randint(0, 1)
    # Define f(x)
    def func(x):
        ret = np.dot(a, x) % 2
        ret = (ret + b) % 2
        return ret
    return func, a , b

def single_test(x):
    """
    Manually set values for a and b to test implementation.
    """
    a = np.array([1, 1, 1])
    b = 1
    ret = np.dot(a, x) % 2
    ret = (ret + b) % 2
    return ret

def test_generator(numTests):
    """
    Generate random values for a and b to test implementation. 
    """
    n = random.randint(1, 4)
    for _ in range(numTests):
        f, a, b = create_func(n)
        print('Real Values: ', a, b)
        bernstein_vazirani(f, n)


if __name__ == '__main__':
    test_generator(5)
