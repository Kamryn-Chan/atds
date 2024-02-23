#!/usr/bin/env python3

"""
atds.py
Contains data structures used in the Advanced Topics CS class.
"""

__author__ = "Kamryn Chan"
__version__ = "2024-02-15"

class Stack():
    """Models a stack using lists
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        """Returns the item on the top of the stack, unless nothing is 
there
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return str(self.stack)


class Queue():
    """Models a queue using lists
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[-1#!/usr/bin/env python3

"""
atds.py
Contains data structures used in the Advanced Topics CS class.
"""

__author__ = "Kamryn Chan"
__version__ = "2024-02-15"

class Stack():
    """Models a stack using lists
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        """Returns the item on the top of the stack, unless nothing is 
there
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return str(self.stack)


class Queue():
    """Models a queue using lists
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def __repr__(self):
        return str(self.queue)
