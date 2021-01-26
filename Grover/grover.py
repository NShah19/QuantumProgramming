import random

def grover(f, n):
    """
    Grover's problem:
    Input: a function f : {0, 1}^n → {0, 1}
    Output: 1 if there exists x ∈ {0, 1}^n such that f(x) = 1, and 0 otherwise
    Notation: {0, 1}^n is the set of bit strings of length n
    """
    # Iterate over all possible binary permuations of n bits
    # keep count of the number of times f(x) returns 1
    # if count = 1, return 1, otherwise, return 0
    count = 0
    max_int = '0b' + '1' * n
    for i in range(0, int(max_int, 2)+1):
        if (f(i) == 1): 
            count += 1 
    if count == 1:
        return 1
    return 0 

def constant_zero(x):
    return 0

def constant_one(x):
    return 1

def create_pass(n):
    # Generate a random number between 0 and 2^n - 1
    golden_val = random.randint(0, (2**n) - 1)
    # Define f(x)
    def one_val(x):
        if x == golden_val:
            return 1
        else:
            return 0

    return one_val

def create_fail(n):
    # Generate a random number between 2 and 2^n - 1
    num_left = random.randint(2, (2**n) - 1)
    # Define f(x)
    def mult_val(x):
        if num_left > 0:
            return 1
        else:
            return 0

    return mult_val

def test_generator(numTests):
    """
    Test implementation for grover's problem.
    """
    n = random.randint(3, 20)
    print('Constant Zero:')
    print(grover(constant_zero, n))
    print('Constant One:')
    print(grover(constant_one, n))
    for _ in range(numTests):
        one_val = create_pass(n)
        print('One value:')
        print(grover(one_val, n))
        mult_val = create_fail(n)
        print('Multiple values:')
        print(grover(mult_val, n))

if __name__ == '__main__':
    test_generator(10)
