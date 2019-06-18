# linked lists 

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
    def set_value(self, value):
        self.value = value

# we'll be figuring out how adding a previous_node property works with a doubly linked list

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a node
        new_node = Node(value)
        # check if we're in an empty list state
        if not self.head and not self.tail:
            # set the list's head ref to the new node
            self.head = new_node
            # set the list's tail ref to the new node
            self.tail = new_node
        else:
            # updtae the old tail's next reference to refer to the new node
            self.tail.set_next(new_node)
            # update the LinkedList's 'tail' reference
            self.tail = new_node
    
    def remove_head(self):
        # what if our list is empty?
        if not self.head and not self.tail:
            return None
        # what if our list only contains a single node?
        if self.head is self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value
        else:
            # store a reference to the node we're removing
            old_head = self.head
            # update the head reference to refer to the old head's next node
            self.head = old_head.get_next()
            # return the old head's value
            return old_head.get_value()

    def contains(self, target):
        #what if our list is empty?
        if not self.head and not self.tail:
            return False
        # get another ref that initially starts at the head of the list
        current = self.head
        # loop so long as 'current' is a valid Node
        while current:
            if current.get_value() == target:
                return True
            #update the current to refer to current's next node
            current = current.get_next()

        #we've looped through the whole list and haven't found what we're looking for
        return False

'''
Tuesday

Text Buffer
-----------
1) add characters from front and back 
2) remove chars from front and back
3) render the contents of buffer
4) concatenate two buffers together (userful for copy/paste

What data structure should we use? What are the trade offs?

        prepend     append  delete_front    delete_back    join     print
DLL     O(1)          O(1)      O(1)           O(1)         O(1)     O(n)  
Array   O(n)          O(1)      O(n)           O(1)         O(n)     O(n)



'''
# import doubly_linked_list

class TextBuffer:

    def __init__(self, init=None):
        self.contents = DoublyLinkedList
        if init:
            for char in init:
                self.contents.add_to_tail(char)

    def __str__(self):
        s=""
        current = self.contents.head
        while current:
            s+= current.value
            current = current.next
        return s
        # no idea what this does, will have to watch again

    def append(self, str_to_add):
        for char in str_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, str_to_add):
        for char in str_to_add[::-1]:
            self.contents.add_to_head(char)
    
    def delete_front(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_head()

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_tail()
    
    def join(self, other_buffer):
        # Connect the tail of this buffer with the head of the other buffer
        self.contents.tail.next = other_buffer.contents.head
        # Set the other buffer's head's previous to be self.tail
        other_buffer.contents.head.prev = self.contents.tail
        # Update other buffer's head to be this buffer's head
        other_buffer.contents.head = self.contents.head
        # Update this buffer's tail to be the other's tail
        self.contents.tail = other_buffer.contents.tail


        