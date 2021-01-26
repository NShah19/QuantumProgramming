from collections import defaultdict 

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
    # Create a dictionary that maps the outputs of f(x) to a list of inputs
    outputToInput = defaultdict(list)
    max_int = '0b' + '1' * n
    # Iterate over all possible binary permuations of n bits, and map outputs to inputs
    for i in range(0, int(max_int, 2)+1):
        input_str = str(format(i, 'b').zfill(n))
        output_str = f(input_str)
        outputToInput[output_str].append(input_str)

    s = ''
    # Iterate over all the items in the dictionary
    for item in outputToInput.items():
        # If each ouput doesn't have two inputs, return 0^n
        if len(item[1]) != 2:
            return '0' * n
        # XOR the two inputs for each output
        y = int(item[1][0], 2) ^ int(item[1][1],2)
        y_str = bin(y)[2:].zfill(n)
        if s == '':
            s = y_str
        # Return 0^n if the XOR'd value doesn't match the previous values
        if s != y_str:
            return '0' * n  

    return s    

def not_2to1_test(x):
    return '111'

def postive_test_1(x):
    # s = '101'
    if x == '010' or x == '111':
        return '010'
    if x == '001' or x == '100':
        return '000'
    if x == '011' or x == '110':
        return '101'
    if x == '000' or x == '101':
        return '110'

def postive_test_2(x):
    # s = '110'
    if x == '010' or x == '100':
        return '000'
    if x == '001' or x == '111':
        return '010'
    if x == '000' or x == '110':
        return '101'
    if x == '011' or x == '101':
        return '110'

def no_s_test(x):
    # no value for s
    if x == '111' or x == '100':
        return '000'
    if x == '001' or x == '010':
        return '010'
    if x == '000' or x == '110':
        return '101'
    if x == '011' or x == '101':
        return '110'

if __name__ == '__main__':
    print(simon(not_2to1_test, 3))
    print(simon(postive_test_1, 3))
    print(simon(postive_test_2, 3))
    print(simon(no_s_test, 3))
