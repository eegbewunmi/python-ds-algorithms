
from linkedlist import LinkedList

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")
llist.prepend("X")

llist.insert_after_node(llist.head.next, "G")
# print(llist.len_iterative())  

# llist.delete_node("B")
# print(llist.delete_node("E"))

# llist.delete_by_position(2)
# llist.print_list()

# llist.node_swap("A", "B")
# print("Swapping nodes A and B where none is head node")
# llist.print_list()

print("")

llist.node_swap("X", "G")
# print("Swapping nodes X and G where X is head node")
# llist.print_list()

# print("")
# llist.reverse_iterative()
# # llist.print_list()

# print("")
# llist.reverse_recursive()
# llist.print_list()

# print(llist.len_iterative())  
# print(llist.len_recursive(llist.head))

llist1 = LinkedList()
llist1.append(-2)
llist1.append(5)
llist1.append(6)
llist1.append(10)
#llist1.print_items()

llist2 = LinkedList()
llist2.append(4)
llist2.append(4)
llist2.append(8)
llist2.append(10)
llist2.append(4)
llist2.append(10)
llist2.append(15)
llist2.append(4)

print(llist2.count_occurrences(4))


#print(merge_lists(llist1, llist2))
# llist1.merge_lists(llist2)

# llist2.remove_duplicates()

# llist1.print_list()

# print(llist1.nth_to_last(6))
        