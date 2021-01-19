def deutsch_jozsa(f, n):
    """
    The Deutsch-Jozsa problem:
    Input: a function f: {0,1}^n → {0,1}.
    Assumption: f is either constant or balanced.
    Output: 1 if f is constant; 0 if f is balanced.
    Notation: {0,1} is the set of bits, and {0,1}^n is the set of bit strings of length n.
    Terminology: 
        Constant: f is constant if either f always outputs 0 or f always outputs 1.
        Balanced: f is balanced if f outputs 0 on exactly half of the inputs.    
    """
    # Generate all possible binary permutations of N bits
    permutations = list(gen_permutations(n))
    # Max number of queries necessary for exact solution: (num permutations)/2 + 1
    max_queries = 2**(n-1) + 1

    # Iterate over binary permutations, counting the ouputs from f 
    count_0 = count_1 = 0
    for i in range(max_queries):
        if f(permutations[i]) == 0:
            count_0 += 1 
        else:
            count_1 += 1

    # If neither 0 nor 1 has been returned by f, we can conclude that f is constant
    # Otherwise, it is balanced
    if count_0 == 0 or count_1 == 0:
        print('f is constant')
        return 1
    else:
        print('f is balanced')
        return 0


# Test functions for f
# Constant functions
def test_all_zero(perm):
    return 0
def test_all_one(perm):
    return 1
# Balanced functions
def test_highest_bit(perm):
    if perm[0] == '0':
        return 1
    else:
        return 0
def test_lowest_bit(perm):
    if perm[-1] == '1':
        return 1
    else:
        return 0
    
def gen_permutations(n):
    """
    generate all the binary permutations with n-length
    """
    max_int = '0b' + '1' * n
    for i in range(0, int(max_int, 2)+1):
        yield str(format(i, 'b').zfill(n))

if __name__ == '__main__':
    deutsch_jozsa(test_all_zero, 3)
    deutsch_jozsa(test_all_one, 3)
    deutsch_jozsa(test_highest_bit, 3)
    deutsch_jozsa(test_lowest_bit, 3)

    deutsch_jozsa(test_all_zero, 15)
    deutsch_jozsa(test_all_one, 15)
    deutsch_jozsa(test_highest_bit, 15)
    deutsch_jozsa(test_lowest_bit, 15)
