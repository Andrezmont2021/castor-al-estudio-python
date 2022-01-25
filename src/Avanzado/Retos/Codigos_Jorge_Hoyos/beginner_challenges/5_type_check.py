# Write a function named only_ints that takes two parameters. 
# Your function should return True if both parameters are integers, and False otherwise.
# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(p1, p2):
    cond1 = type(p1)
    cond2 = type(p2)
    if cond1 == int and cond2 == int:
        print(True)
        return True
    else:
        print(False)
        return False

only_ints(1, "a")