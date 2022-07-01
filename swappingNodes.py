import Node
import LinkedList

def swap_nodes(input_list, val1, val2):
  '''This function first takes in the values val1 
and val2 which are to be swapped.'''
  print(f'Swapping {val1} with {val2}')
  '''node1_prev and node2_prev are the nodes that 
have pointers set towards node1 and node2'''
  node1_prev = None
  node2_prev = None
  '''Then we start by placing both the node1 and 
node2 values as the HEAD OF THE LIST.'''
  node1 = input_list.head_node
  node2 = input_list.head_node

  '''Here, we are checking whether or not the two 
values inputted are the same or not. This is an edge case.'''
  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  '''Here, we are starting the iteration of the 
input_list where node1 is the head_node and checking 
whether or not node1 is in fact val1. If so, we break 
the loop, else, we assign node1 as node1_prev and make 
node1 the next_node, and it will continue till val1 is 
found. The same is True for node2.'''
  while node1 is not None:
    #as we can see, it does not matter what the placement 
#of node1 is for this while loop, as it is not setting node1 
#as the head node, it is only storing whether or not node1's 
#value is equivalent to the value being provided.
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()
    
  '''This is another edgecase as we are 
taking into consideration where there is no 
node such as node1 or node2, which would make 
the swapping impossible.'''
  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return
  '''This is when we check either there is in 
fact a node before node1 or node2. If node1 does 
not have a previous, then it implies that it was 
the head of the list, so now, node2 will be the 
head of the list.'''
  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)
  '''Now, we are just swapping the following nodes of each of node1 and node2.'''
  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)


ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())


#RESULT#
#9
#8
#7
#6
#5
#4
#3
#2
#1
#0
#
#Swapping 9 with 5
#5
#8
#7
#6
#9
#4
#3
#2
#1
#0