# We'll be using our Node class
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

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    #first we are checking whether or not the head node 
    # is the node that is being asked to remove
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      #while there is a current_node, and it is also not the 
      # node that is to be removed, we go check for the next node
      while current_node:
        #we create a new variable called the next_node and set 
        # its value as the next node after the head_node by using the get_next_node method
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          # we are setting the next node after the current head 
          # node as the next node after it and turning the current_node to
          # None to end the loop. As we set a next_node and remove itself 
          # from the list, the next_node takes it place before it turns to None. 
          # it specifically uses the SET_NEXT_NODE method as opposed to the 
          # GET_NEXT_NODE as it is replacing it.
          current_node.set_next_node(next_node.get_next_node())
          #we are setting it to None to exit the loop
          current_node = None
        else:
          current_node = next_node