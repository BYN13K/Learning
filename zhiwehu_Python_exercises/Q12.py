"""
Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


res = []
for i in range(1000, 3001, 2):
  res.append(str(i))

print(",".join(res))


sol.. nawet dla danych z input wystarczy sprawdzic pierwsza liczbe czy jest pazysta wiec nie wiem o co tu chodzi
Trzeba sprawdzic karzda cyfre w liczbie czy jest pazysta..
Kod z odpowiedzi- nie ma sensu przepisywac
"""

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (
            int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        values.append(s)
print(",".join(values))
