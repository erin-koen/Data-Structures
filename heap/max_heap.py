class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # swap first and last items in the array (root for meaningless leaf)

        self.storage[0], self.storage[len(
            self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]

        # pop off the last item in the array, has to happen before the sift so you need to store it in a variable to return
        biggest = self.storage.pop()

        # sift down the new top item in array
        self._sift_down(0)

        # return the former topmost value
        return biggest

    def get_max(self):
        print(self.storage)
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # recieves an index, which is where the value currently is
        # keep bubbling up till we've reached the top of the heap or we've reached a point where the parent is higher priority.
        # on a single bubble up iteration, we are going to get the parent index, compare the child index's value against teh value of the parent.
        # if the child value is higher priority, then swap them, else child is at valid spot, stop bubbling.
        while index > 0:
            parent = (index-1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # update the child's index to reflect swap
                index = parent
            # otherwise the child is at a valid index.
            else:
                break

    def _sift_down(self, index):

        # declare the children

        left = 2*index+1

        right = 2*index+2

        # keep going till we compare the parent of the last node in the list
        while left <= len(self.storage)-1 and right <= len(self.storage)-1:

            # if the item at storage[index] is less than either of its children, swap it with the larger of the two.

            if self.storage[index] < self.storage[left] and self.storage[left] >= self.storage[right]:
                self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
                index = left
                left = 2*index+1
                right = 2*index+2

            elif self.storage[index] < self.storage[right] and self.storage[right] >= self.storage[left]:
                self.storage[index], self.storage[right] = self.storage[right], self.storage[index]
                index = right
                left = 2*index+1
                right = 2*index+2

            else:
                break
