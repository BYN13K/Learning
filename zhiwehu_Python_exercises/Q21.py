# ### Question 21
# Level 3

# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
##############
# spilt ' ' 
# if 'UP' in string'
# input from consol

import math

position = [0,0]
while True:
    move = (input(f"set direction UP, DOWN, LEFT, RIGHT and the amaund of steps or 'q' for print distance nad quit: ")).upper()
    move = move.split(' ')
    print(move)
    if 'UP' in move:
        position[0] += int(move[1])
    elif 'DOWN' in move:
        position[0] -= int(move[1])
    elif 'LEFT' in move:
        position[1] += int(move[1])
    elif 'RIGHT' in move:
        position[1] -= int(move[1])
    elif move[0] == 'Q':
        print(f"Distance from start position is {math.sqrt((position[0]^ 2) + (position[1] ^ 2)) }")
        break
    

