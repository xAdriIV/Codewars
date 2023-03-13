# number1 = [0,0,0,0,1]Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
# Examples:
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

def binary_array_to_number(arr):
    total = 0
    i = 1
    for num in arr[::-1]:
        total += (i*num)
        i *= 2
    return total
print(binary_array_to_number([0, 0, 0, 1]))

# USING MAP() Map function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Syntax :
# map(fun, iter)

def binary_array_to_number2(arr):
    return int("".join(map(str, arr)), 2)
print(binary_array_to_number2([1, 0, 1, 1]))
