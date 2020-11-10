# ### Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield
######
# Generujemy tylko liste liczb podzielnych przez  7 lub całą liste i sprawdzamy karzdy obiekt

zakres = (input(f"enter the beginning and end of the range separeted whit ',' :  ")).split(',')
start = int(zakres[0])
end = int(zakres[1])

serch = True
while serch:
    for seven in range(start, end):
        if (seven % 7) == 0:
            start = seven
            serch = False
            break

for i in range(start, end, 7):
    print(i)



# def numbers(n):
#     i = 0
#     while i<n:
#         if i%7==0:
#             yield i    # return powoduje bład, ewentualnie odrazu print
#         i += 1

# for i in numbers(100):
#     print(i)
