"""
### Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""

class meth:

    def __init__(self):
        self.in_str = ""

    def get_string(self):
        self.in_str = input("Pleaz input text: ")

    def print_string(self):
        print(self.in_str.upper())

m = meth()

m.get_string()

m.print_string()
