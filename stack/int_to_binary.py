from stack import Stack


'''Creating a function to convert and integer to binary, the binary values
woud be stored in a stack so the values can be printed easily'''
# using while loop
def convert_to_binary(dec_num):
    if dec_num == 0:
        return 0
    
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

#Using recursion
def int_to_binary(integer_value):
    s = Stack()
    bin = ""

    if integer_value == 0:
        while not s.is_empty():
            bin += str(s.pop())
        return bin
        

    rem = integer_value % 2
    s.push(rem)
    integer_value = integer_value // 2

    return int_to_binary(integer_value)
 
    


print(int_to_binary(242))
print(int_to_binary(56))
print(int_to_binary(2))
print(int_to_binary(32))
print(int_to_binary(10))
print(int_to_binary(0))
print(int(int_to_binary(56),2)==56)