# ### Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

pas_seq = input("enter passwords separated whit ','. Passwor requider 6-12 charakters a list 1 uper leter 1 lower leter one number and one of($#@)")

passwords = pas_seq.split(',')
spec = ['$','#','@']
passing = []

for p in passwords:
    if 6 <= len(p) <= 12:
        a = False
        b = False
        c = False
        d = False
        for char in p:
            if char.isnumeric():
                a = True
            elif char in spec:
                b = True
            elif char.isupper():
                c = True
            elif char.islower():
                d = True
        
        if a and b and c and d:
            passing.append(p)

print(','.join(passing))

