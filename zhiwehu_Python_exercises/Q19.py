# ### Question 19
# Level 3 TODO zrobic BST

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. 
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
##################################################################
# dane wejsciowe dzielimy ',' i zapisujemy w formie (str,int,int)
# porwonujemy [0] i gdy jest rowne to [1] itd..
# binary tree?? - mozna sortowac przy wprowadzaniu danych. - TODO komenda drukoania - przerost formy nad zadaniem
# zwykła lista tez da rade - sortowanie przy wprowadzaniu danych skomplikuje (zalatwi) sprawe- przeliczanie przy kazdym wprowadzeniu
# albo zwykla lista, albo BST

# Zwykla lista z sorted()

users = []

while True:
    person = input(f"Pleaz input 'personname,age,height' to add person, 'p' - print all persons, 'e' - end:   ")
    if len(person) == 1:
        if person.lower() == 'p':
            print(sorted(users))
        elif person.lower() == 'e':
            break
    elif len(person) >= 5:
        person = person.split(',')
        person[1] = int(person[1])
        person[2] = int(person[2])
        users.append(tuple(person))
    
        