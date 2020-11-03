# ### Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

account = 1000
cont = True
print("Please input transaction whit the format 'X YYYY' where:")
print("'X' is 'D' for deposit or 'W' for withdraw")
print("'Y' is amount of transaction")
print("You can use 'B' for account balanc or 'Q' for quit")

while cont:
    

    trans = input("Please input transaction 'X YYYY': ")
    print(trans[0].upper())

    if trans[0].upper() == 'D':
        account += int(trans[1:])
    elif trans[0].upper() == 'W':
        if account >= int(trans[1:]):
            account -= int(trans[1:])
        else:
            print(f"You hawe {account} on your acc. You can't withdraw {int(trans[1:])}")
    elif trans[0].upper() == 'B':
        print(f"Your account balance is: {account}")
    elif trans[0].upper() == 'Q':
        break
    else:
        print("Please select 'D' , 'W' , 'B' or 'Q' at beginning")
