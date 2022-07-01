# We'll be using the Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# LinkedList class
class LinkedList:
  #we are initializing the new LinkedList class
  def __init__(self, value=None):
    self.head_node = Node(value)
  #this function is for getting the head node
  def get_head_node(self):
    return self.head_node
  

#we use this function to insert a new head node
  def insert_beginning(self, new_value):
    print('Printing new value:', new_value)
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
#the purpose of this function is to get a 
# string list of all the nodes within the 
# linked_list and it starts with the current 
# head_node and is carried out till the oldest 
# headnode. It uses the while loop to add the 
# newline function
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    print('Printing the current_node of the head_node, which is 90 at the latest:', current_node)
    while current_node:
      if current_node.get_value() != None:
        print('Printing current_node:', current_node.get_value(), current_node)
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  

# Testing code
    
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
print('-' * 20)
print('The 90 gets printed as the first term now as it is replacing 5675 which had replaced 70 which had replaced 5 as the previous headnodes. Instead of deleting the previous data, the inserting_node function helps to store the previous data in the data structure while also making room for the newer head_nodes.')