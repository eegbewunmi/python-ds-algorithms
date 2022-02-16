''' Stacks have items placed on top of one another, enabling you to 
access only the top element at a time. So to get the bottom element, you keep
removing from the top (First In Last Out)
'''
'''Here i'll be using a list to create a stack data structure'''

class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    #push method
    def push(self, value):
        self.stack.append(value)

    #pop method
    def pop(self):
        return self.stack.pop()

    #peek operation
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    #return the stack items
    def get_stack(self):
        return self.stack

    #check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# myStack = Stack()
# print(myStack.is_empty()) 
# myStack.push("A")
# myStack.push("B")
# print(myStack.get_stack())
# myStack.push("C")
# print(myStack.get_stack())
# myStack.pop()
# print(myStack.get_stack())
# print(myStack.is_empty()) 
# print(myStack.peek())