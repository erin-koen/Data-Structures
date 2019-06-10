'''
Understand
----------
A queue is an ordered list. They're FIFO. Items get added to the back of the list, and taken off the front.
- dequeueing == changing the second to last item in the list's next reference to Null.
- enqueing == adding a new node with a next reference to the current head.
- need to control for insertion? In other words, find a way to explicitly disallow it?
- what happens when there's only one node? Or how do you instantiate a queue form nothing? What's the first node?

Plan
----
- create a Node class, create a LinkedList Class, then create Queue as a subclass of LinkedList with the QUeue-specific functions

*** IGNORE ALL THAT, DO IT AS A LIST***


'''

class Queue():
    def __init__(self):
        self.size = 0
        self.storage = []


    def enqueue(self, item):
        self.storage.insert(0, item)
        
    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

    def len(self):
        return len(self.storage)
