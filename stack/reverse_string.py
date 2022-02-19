''' Given a string, this function will reverse the string e.g 'Hello' becomes 'olleH' '''
from stack import Stack

def reverse_string(str):
    # creating a stack object
    s = Stack()
    reverse_str = ""

    if str == "":
        return None

    else:
        for value in str:
            s.push(value)

    while not s.is_empty():
        reverse_str += s.pop()

    return reverse_str

# input_str = "!evitacudE ot emocleW"
# print(reverse_string(input_str))