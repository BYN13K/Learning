"""
### Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def check_binar(binar):
  
  if len(binar) == 4:
    binar = list(set(binar))
    if binar == [0,1] or binar == [1] or binar == [0]:
      return True
    else:
      return False

def check(text):
  text = text.split(",")
  print(text)
  for n in text:
    s = [int(x) for x in n]
    
    if check_binar(s) == True:
      if (int(n, 2)%5) == 0:  #zastosowanie parametru zmiany bin na dec - int(x, 2)
        print(f'Resultat prawdziwy {n} jako bin {int(n, 2)}')

a = "0100,0011,1010,1001"

check(a)

"""
Solution:
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))

"""
