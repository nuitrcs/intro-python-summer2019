# FUNCTIONS exercises

# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top


# Write a function called print_multiples that takes as input a string and a number (give the parameters names);
# have the function print the string the specified number of times.
# Hint: remember string multiplication?
def print_multiples(val, times):
    print(val*times)


# call the function
print_multiples("dog", 3)
print_multiples("cat", 0)


# Write a function called "ceiling" that takes two inputs: a value, and a parameter "maxval"
# with a default value of 10.  If the value is less than the ceiling, return the value;
# otherwise return the maxval
def ceiling(val, maxval=10):
    if val <= maxval:
        return val
    return maxval


# call it
print(ceiling(8))
print(ceiling(12))
print(ceiling(3.4, 1))