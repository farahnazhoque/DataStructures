class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Add your code below:

if __name__ == '__main__':
  yacko = Node("likes to yak")
  
  wacko = Node("has a penchant for hoarding snacks")
  dot = Node("enjoys spending time in movie lots")
  
  '''as we are setting dot and yack nodes
  to wacko and dot respectively when we try 
  to retrieve dots_data we can use yacko's node to get it.'''
  
  dot.set_link_node(wacko)
  yacko.set_link_node(dot)

  dots_data = yacko.get_link_node().get_value()
  wackos_data = dot.get_link_node().get_value()
  
  print(dots_data)
  print(wackos_data)