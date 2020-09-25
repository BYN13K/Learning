"""
### Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

class line_cap:

    def __init__(self):
        self.line = []

    def add_line(self):
        line = input('Input a line: ')
        self.line.append(line)

    def pirnt_line(self):
        n_line = 0
        while n_line == 0:
            n = int(input(f'You hawe {len(self.line)} lines. Choose line to print: '))
            if 0 < n >= len(self.line):
                n_line = n
            else:
                print(f'Select number of line (1 - {len(self.line)})')

        line = self.line[n_line-1]
        print(line.upper())


    def print_all(self):
        for l in self.line:
            print(l.upper())

line = line_cap()

line.add_line()
line.add_line()
line.add_line()
line.add_line()

line.pirnt_line()

line.print_all()

"""
Mozna to zrobic bez class i def jak petle - z odpowiedzi

Solution:
```python
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
"""