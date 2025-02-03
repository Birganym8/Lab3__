import itertools

def print_permutations(s):
  
    permutations = itertools.permutations(s)
    

    for perm in permutations:
        print(''.join(perm))


x = input("Enter a string: ")
print("All permutations of the string are:")
print_permutations(x)

