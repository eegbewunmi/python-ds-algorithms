''' Every linkedlist has nodes so i'll be creating a node class and linkedlist class Basically an empty linked list'''

class Node:
    '''Each Node consists of dtat and a pointer (next) to the next node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''The head is a pointer to the first node in the linkedlist'''
    def __init__(self):
        self.head = None

    def append(self, data):
        ''' adding data to the end of a linked list'''
        new_node = Node(data)
        #if the linkedlist is empty
        if self.head is None:
            self.head = new_node
            return

        #if it's not empty, traverse through it to get the last node
        head_node = self.head
        while head_node.next:
            head_node = head_node.next
        head_node.next = new_node

    def print_list(self):
        '''printing the data in the list on each line'''
        current_node = self.head
        while current_node:
            print (current_node.data)
            current_node = current_node.next

    def prepend(self, data):
        '''Add data to the beginning of the linkedlist'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        '''Given a particular node, insert a new node after it, the input is a 
        node, not its data, e.g self.head.next.next'''
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_node(self, data):
        '''Deleting by Value'''
        '''Given the data a node contains, delete the node'''
        #if the node is the head
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = self.head.next
            '''Even though i have changed the head of the node, the previous head still points to it so we have to remove the link or say that nothing(None) points to the new head'''
            current_node = None 
            return

        #if any other node asides the head
        
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            
        return('Node {} not found in linked list'.format(data))





llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")

llist.insert_after_node(llist.head.next, "G")

llist.delete_node("D")
llist.delete_node("B")
print(llist.delete_node("E"))

llist.print_list()  


        