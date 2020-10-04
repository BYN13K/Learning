"""
Question 13
Level 2

Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""
t = input()

dig = 0
let = 0

for z in t:
  if z.isdigit():
    dig += 1
  elif z.isalpha():
    let += 1


print("LETTERS: " + str(let) + "  DIGITS: " + str(dig))
