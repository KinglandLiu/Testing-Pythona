'''
Project 3 - Guess that number

random_number = random()

input in range (1-10)
check input == random_number
check input < max range
input in range (1-10)
check input > least range 
input in range (1-10)
'''

import random 
MAX = 10
MIN = 1

random_number = random.randint(MIN, MAX) 


def getInput():
    return int(input(f"Enter number between {MIN}-{MAX}:"))

def main():
# START OF FUNCTION
    user_input = getInput()
    if user_input == random_number:
        print("You Found The Number!")
        return
    elif user_input < MIN:
        print("Input number greater than", MIN)
    elif user_input > MAX:
        print ("Input number less than", MAX)
    else:
        print("Try Again!")
    main()
# END OF FUNCTION

main() 
