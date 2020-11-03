"""
Question 15
Level 2

Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""
con = True


def count():
    a = input('Pleas input a number:')

    if a.isdigit() and len(a) == 1:
        a = int(a)
        doble = int(str(a) * 2)
        triple = int(str(a) * 3)
        forth = int(str(a) * 4)
    else:
        print("Pleas input silgle number")
    print(a+doble+triple+forth)

while con:
    count()
    repet = input("Again? (Y/N):")
    if repet.lower() == "y" :
        continue
    else:
        con = False 
