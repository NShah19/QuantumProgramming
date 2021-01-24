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
           print("f(x) = 1 for ", str(format(i, 'b').zfill(n)))
           return 1
    return 0 

def negative_test(x):
    return 0

def positive_test(x):
    return 1

def create_func(n):
    # Generate a random number between 0 and 2^n - 1
    golden_val = random.randint(0, (2**n) - 1)
    golden_val = format(golden_val, 'b').zfill(n)
    # Define f(x)
    def func(x):
        if x == golden_val:
            return 1
        else:
            return 0 
    return func, golden_val

def test_generator(numTests):
    """
    Generate random value for n and golden value to test implementation. 
    """
    n = random.randint(3, 20)
    print('Negative Test:')
    print(grover(negative_test, n))
    print('Positive Test:')
    print(grover(positive_test, n))
    for _ in range(numTests):
        f, golden_val = create_func(n)
        print('Golden Value: ', golden_val)
        grover(f, n)

if __name__ == '__main__':
   test_generator(10)
