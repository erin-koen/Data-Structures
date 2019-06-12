class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # recieves an index, which is where the value currently is
    # keep bubbling up till we've reached the top of the heap or we've reached a point where the parent is higher priority.
    # on a single bubble up iteration, we are going to get the parent index, compare the child index's value against teh value of the parent.
    # if the child value is higher priority, then swap them, else child is at valid spot, stop bubbling. 
    while index > 0:
        parent = (index-1) // 2
        if self.storage[index] > self.storage[parent]:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            #update the child's index to reflect swap
            index = parent
        # otherwise the child is at a valid index.    
        else: 
            break


  def _sift_down(self, index):
    pass
