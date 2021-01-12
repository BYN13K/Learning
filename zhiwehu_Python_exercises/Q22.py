# ### Question 22
# Level 3

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1  #todo pozbyc sie znakow interpunkcyjnych
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.


sentence = input("Put your sentenc to analyze: ")

inter = (',', '.', '?', '!', '@')

for i in inter:
    sentence = sentence.replace(i, "")

# sentence = sentence.split(" ")

output = {}

for word in sentence.split(" "):
    
    if word not in output:
        output[word] = 1
    else:
        output[word] += 1
    
for word in output:
    print(f"{word}:{output[word]}")