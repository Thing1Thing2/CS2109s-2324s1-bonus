import heapq

class PriorityQueue:
    """A Queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first.
    If order is 'min', the item with minimum f(x) is
    returned first; if order is 'max', then it is the item with maximum f(x).
    Also supports dict-like lookup."""
    def __init__(self, order='min'):
        self.heap = []
        if order == 'min':
            pass
        elif order == 'max':  # now item with max f(x)
            raise NotImplementedError
        else:
            raise ValueError("Order must be either 'min' or 'max'.")

    def append(self, item, val):
        """Insert item at its correct position."""
        heapq.heappush(self.heap, (item, val))
        

    def extend(self, items):
        """Insert each item in items at its correct position."""
        for item in items:
            self.append(item[0], item[1])
        
    def pop(self):
        """Pop and return the item (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        """Return current capacity of PriorityQueue."""
        return len(self.heap)

    def __contains__(self, key):
        """Return True if the key is in PriorityQueue."""
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        """Returns the first value associated with key in PriorityQueue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)
        
    def print(self):
        print(heapq.nsmallest(self.heap.__len__(), self.heap))
