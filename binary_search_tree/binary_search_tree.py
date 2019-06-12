class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # compare element against the current node's value
    # based on the result of the comparison, go left or right
    # if we find an empty spot, park the value there
    # otherwise go back to step 1
    # What is the base case? We've found an empty spot where we can add the value
    if value < self.value:
        # if the value's left, we go left
        # if there's no left child, we can part value here
        if not self.left:
            self.left = BinarySearchTree(value)
            #recurse on left child
        else: 
            self.left.insert(value)
    
    elif value > self.value:
        if not self.right:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)


  def contains(self, target):
      # compare the element against the node's value
      # based on the result of the comparison, go left or right
      # if we find the target, return True
      # if we try to move a direction sans node, we've reached the end and return false
    if target == self.value:
        return True
    elif (target < self.value and not self.left) or (target > self.value and not self.right):
        return False
    else: 
        if target < self.value:
            return self.left.contains(target)
        elif target > self.value:
            return self.right.contains(target)

  def get_max(self):

      # base case - if get_max is called on a node which has no right node, it is the biggest in the tree. Return that node's value.
    if self.right is None:
        return self.value
    else: 
        return self.right.get_max()


  def for_each(self, cb):
    pass
