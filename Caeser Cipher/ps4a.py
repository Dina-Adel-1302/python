# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #pass #delete this line and replace with your code here
    
    # Base case:
    # if ​sequence ​ is a single character, there’s only one way to order it
    #  return a singleton list containing sequence
    if len(sequence) == 1:
        return sequence
   
    #recursive case: 
    # all subsets without first element!
    perm = get_permutations(sequence[1:])
    #print("perm:", perm)
    #create a string of just fist element !
    first_char = sequence[:1]
    new = []
    for l in perm:
        new.append(first_char + l)
        for i in range(len(l)):
            new.append(l[i:] + first_char + l[:i])
            #new.append(l[i:] + first_char)
            # new.append(first_char + l)
        #new.append(l + first_char)
        #     
            # 
        #print("new:", new)
    
    return new 

if __name__ == '__main__':
    
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    #EXAMPLE
    example_input = 'ust'
    print('Input:', example_input)
    print('Expected Output:', ['tus', 'tsu', 'uts', 'ust', 'stu', 'sut'])
    print('Actual Output:', get_permutations(example_input))
    
    #EXAMPLE
    example_input = 'wfy'
    print('Input:', example_input)
    print('Expected Output:', ['wfy', 'fyw', 'ywf', 'wyf', 'yfw', 'fwy'])
    print('Actual Output:', get_permutations(example_input))
    

    #pass #delete this line and replace with your code here

