"""
### Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

"""
nums = []

for n in range(2000,3201):
    if n % 7 == 0 and n % 5 != 0:
        nums.append(str(n))

print('.'.join(nums))
