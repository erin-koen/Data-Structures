"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # if the DLL is empty, must create a new node and set head and tail = it
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:    
            # call the current head node's *insert_before* method
            self.head.insert_before(value)
            #change the DLL's head to the new node (which will be stored in the old node's *prev* after the method above is executed)
            self.head = self.head.prev
            # increment length of DLL
            self.length += 1

    def remove_from_head(self):
        if self.length == 0:
            # handles some weird error in the test where it's returning an object that shouldn't be there.
            self.head = None
            self.tail = None
            return None
        # if there are nodes in the list, declare variables before you change anything. one to set the head to, one to return
        new_head = self.tail.prev
        val = self.head.value
        # call delete on current tail (sets tail.prev's next val to None)
        self.tail.delete()
        # if this is only node in the list, set self.tail and self.head to None, decrement list (or set to 0)
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        else:    
            # capture head node's value to return when finished
            val = self.head.value
            # store current head's prev to set to DLL head once delete finished
            new_head = self.head.prev
            # delete old head (changes prev ref in next node to None, but according to method above doesn't change the next ref in old head to None, is that bad?)
            self.head.delete()
            # Set DLL's head to the new_head declared above
            self.head = new_head
            # decrement length
            self.length -= 1
            
        return val

    def add_to_tail(self, value):

        # if DLL is empty, create a new node and set it equal to head and tail
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # call insert_after on current tail
            self.tail.insert_after(value)
            # declare a new tail variable
            new_tail = self.tail.next
            # set DLL's tail to new tail
            self.tail = new_tail
            # increment lenght
            self.length += 1

    def remove_from_tail(self):
        # if there are no nodes in the DLL, return none
        if self.length == 0:
            return None
        # if there are nodes in the list, declare variables before you change anything. one to set the tail to, one to return
        new_tail = self.tail.prev
        val = self.tail.value
        # call delete on current tail (sets tail.prev's next val to None)
        self.tail.delete()
        # if this is only node in the list, set self.tail and self.head to None, decrement list (or set to 0)
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:    
            # set tail = new_tail
            self.tail = new_tail
            # decrement the DLL length
            self.length -= 1
            # return value of deleted tail
        return val

    def move_to_front(self, node):
        # references a node in the list, so if there are only two, they'll be swapping
        if self.length == 2:
            front = ListNode(self.tail.value)
            back = ListNode(self.head.value)
            front.next = back
            back.prev = front
            self.head, self.tail = front, back
        else:
            # call insert before on current head
            self.head.insert_before(node.value)
            # delete the refs to the node being moved
            node.delete()
            # set the DLL's head to the node being moved
            self.head = self.head.prev



    def move_to_end(self, node):
        # references a node in the list, so if there are only two, they'll be swapping
        if self.length == 2:
            front = ListNode(self.tail.value)
            back = ListNode(self.head.value)
            front.next = back
            back.prev = front
            self.head, self.tail = front, back
        else:
            # call insert after on the current tail
            self.tail.insert_after(node.value)
            # delete the refs to the node being moved
            node.delete()
            # set the DLL's tail to the node being moved
            self.tail = self.tail.next

    def delete(self, node):
        # handle the DLL's head and tail
        if self.length == 1:
            self.head = None
            self.tail = None
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        
        node.delete()
        self.length -= 1

    def get_max(self):
        # declare a variable to return
        big = None
        # declare a variable to count against length and measure the loop (length is not zero indexed)
        count = 1
        # declare a variable to figure out which node is next in the list
        next_node = None
        # handle the zero node list edge case
        if self.length == 0:
            return None
        # handle the 1 node list edge case
        elif self.length == 1:
            big = self.head.value
        # while loop to measure node value vs big variable    
        while count <= self.length:
            # start the loop on the head
            if next_node == None:
                big = self.head.value
                next_node = self.head.next
                count += 1
            # for every other node
            else:
                if next_node.value > big:
                    big = next_node.value
                next_node = next_node.next
                count += 1
        return big


