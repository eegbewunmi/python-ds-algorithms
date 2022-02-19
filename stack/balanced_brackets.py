''' CReating a function to check if a string is balanced, i'll be using
a stack to implement this. The stack class has been created in stack.py'''

#importing the stack class
from stack import Stack

def is_match(value, top_element):
    ''' This is a function to chek if the closing bracket
    matches the open bracket currently the top element of 
    the stack'''

    if value == '}' and top_element == '{':
        return True
    elif value == ')' and top_element == '(':
        return True
    elif value == ']' and top_element == '[':
        return True
    else:
        return False
    
#e.g brac_string = '[{}]()'
def is_balanced(brac_string):
    ''' function for checking if a given string (brac_string) containing only brackets is balanced'''
    s = Stack()

    for value in brac_string:
        if value in '{([':
            s.push(value)
        else:
            if not s.is_empty():
                if is_match(value, s.peek()):
                    s.pop()
                else:
                    return False
            else:
                return False
   
    if s.is_empty():
        return True
    else:
        return False



# print("String : (((({})))) Balanced or not?")
# print(is_balanced("(((({}))))"))

# print("String : [][]]] Balanced or not?")
# print(is_balanced("[][]]]"))

# print("String : [][] Balanced or not?")
# print(is_balanced("[][]"))

# print("String : [[][] Balanced or not?")
# print(is_balanced("[[][]"))