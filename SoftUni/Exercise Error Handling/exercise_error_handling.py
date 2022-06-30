import sys
from io import StringIO

input1 = """one
1
two
2
Search
one
Remove
two
End
 
"""
input2 = """one
two
Search
Remove
End

"""
input3 = """one
1
Search
one
Remove
two
End

"""

sys.stdin = StringIO(input3)

numbers_dictionary = {}

line = input()
# this while loop add number to dictionary
while line != "Search":
    number_as_string = line
    # add try-except for ValueError and print a message
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = input()  # add this row to read string input in while loop

line = input()
# this while loop search and print number by key string
while line != "Remove":
    # replace variable name from "searched" to "searched_number_to_print"
    searched_number_to_print = line
    print(numbers_dictionary[searched_number_to_print])
    line = input()  # add this row to read string input in while loop

line = input()
# this while loop remove number by key string
while line != "End":
    # replace variable name from "searched" to "searched_number_to_delete"
    searched_number_to_delete = line
    # add try-except for KeyError and print a message
    try:
        del numbers_dictionary[searched_number_to_delete]
    except KeyError:
        print('Number does not exist in dictionary')
    line = input()  # add this row to read string input in while loop

# print dictionary elements
print(numbers_dictionary)
