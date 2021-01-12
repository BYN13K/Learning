"""### Question 31
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
"""

def func(a, b):
    if len(a) > len(b):
        print(a)
    elif len(a) < len(b):
        print(b)
    else:
        print(a)
        print(b)

func('jeden', 'dwa')