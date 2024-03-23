
print("pee pee poo poo") # This is my first line of Python code
# This line (starts w/ #) is a comment, which is NOT read by the computer
'''
Therefore, comments can be used as notes to self or other programmers 
in order to better understand what things do.
This text right here a multi-line quote, set off by the three single 
quotes and enclosed by three single quotes as well.
Multi-line comments are also not read by the computer and very useful 
at the beginning of programs for full project explanation if necessary.
'''
# a string is anything in quotes so "a", 'word', "a sentence", and '1' are all strings
string="word"   

# an integer is any whole number so -2, -1, 0, 1, 2 are all integers
integer=1  

# a float is any non-whole number, meaning 0.1, 1.1, 1.11, 11.11 are all floats
a_float=1.2 

print("{} is type: {}".format(string, type(string)))
print("{} is type: {}".format(integer, type(integer)))
print("{} is type: {}".format(a_float, type(a_float)))

# Important example talked about above
print("'This is a string', Michael said")

'''
Integers and floats can have mathmatical operations done on them such as +,-,/,*
A coding specific one is modulus (%) which gets just the *remainder* of division
For example, to check if a number is even, you could do num % 2 and if it returns 0 it is even
'''
a_list=[1, "2", 3.0] 
# this is a list, it can be made up of a combination of any of the variable types

print("At index {}, retrieved {} which is type: {}".format(0, a_list[0], type(a_list[0]))) 
# the [] after the list name indicates what index (spot in the list) that you want to access

print("At index {}, retrieved {} which is type: {}".format(1, a_list[1], type(a_list[1]))) 
# the index always starts at 0 so the length of the list is n-1
      
print("At index {}, retrieved {} which is type: {}\n".format(2, a_list[2], type(a_list[2])))
# the \n at the end of the string tells the computer to add another line underneath the text

# You can also use the contents of the list to find its own index, for example:
index_of_two=a_list.index("2") # .index() is used to find the index of an element on a list
print("{} is the index location for {} in the list".format(index_of_two, "2"))

# Lastly, you can append elements to the end of the list, for example:
a_list.append("added")
print("This is the list after 'added' was appended to the end of the list: ", a_list)

# You can also remove elements of the list
a_list.remove('2')
print("This is the list after '2' was removed from the list: ", a_list)

# You can also get the length of the list
# As well as every variable type in python so this next command is very helpful
length_of_list=len(a_list)
print("The length of the list after an element was added is: ", length_of_list)
