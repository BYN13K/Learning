"""
Level 2

Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""

t = input(f'Input text:  ')

up = 0
low = 0

for l in t:
  if l.isupper() and l.isalpha():
    up += 1
  elif l.islower() and l.isalpha():
    low += 1

print('UPPER CASE: ' + str(up) + '  LOWER CASE: ' + str(low))