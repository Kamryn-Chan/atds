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
        """Returns the item on the top of the stack, 
        unless nothing is there.
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

class Deque(object):
    def __init__(self):
        self.deque = []
    
    def add_front(self, item):
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0

class Node(object):
    """Defines a node class to be used in an
    UnorderedList, coming soon.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"

class UnorderedList(object):
    """Maintains an unordered list via a linked 
    series of Nodes.
    """
    def __init__(self):
        self.head = None

    def add(self, new_data):
        """Creates and adds a new Node to the beginning
        of the list.
        """
        temp_node = Node(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def length(self):
        """Returns the number of nodes in the list.
        """
        node_count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            node_count += 1
        return node_count

    def search(self, data):
        """Returns true if the data is found on the list.
        """
        current = self.head
        while current != None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, data):
        """Removes multiple occurrences of data on the list, 
        which requires going through the entire list until
        you hit the end, or nothing if the data isn't on the list.
        """
        current = self.head
        previous = None
        while current != None and self.head != None:    # Have to search entire list
            if current.get_data() == data:              # need to remove it
                if previous == None:                    # we're at the head
                    self.head = current.get_next()
                    current = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:                                       # pass on through
                previous = current
                current = current.get_next()

    def is_empty(self):
        return self.head == None

    def append(self, data):
        """Appends an item to the end of the list
        """
        temp = Node(data) 
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, data):
        """Returns the index of the first occurence of the data
        in the list.
        """
        if self.head == None:
            return None
        current = self.head
        index = 0
        while current != None and current.get_data() != data:
            current = current.get_next()
            index += 1
        if current == None:
            return None
        else:
            return index

    def insert(self, position, data):
        """Inserts the piece of data at the indicated position.
        """
        temp = Node(data)
        index = 0
        current = self.head
        previous = None
        while index < position:
            previous = current
            current = current.get_next()
            index += 1
        if index == 0:
            temp.set_next(current)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)

    def pop(self, index=-1):
        """Removes item at position index, or at the end of the list
        (-1) if no index is indicated.
        """
        if self.head == None:
            return None      # Can't pop from empty list
        if index == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif index == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:       # returning from middle of list?
            current = self.head
            previous = None
            position = 0
            while position < index:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result

    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result


class UnorderedListStack(object):
    """Implements a Stack using the UnorderedList class.
    """
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        """Pushes an item onto the top of the stack.
        """
        self.ul.add(item)

    def pop(self):
        """Removes the item at the top of the stack and
        returns it.
        """
        return self.ul.pop(0)
    
    def peek(self):
        """Examines the item at the top of the stack
        and returns that value. 
        """
        value = self.ul.pop(0)
        self.ul.add(value)
        return value

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()

def main():
    print("Testing the Stack class") 
    testsPassed = 0
    try:
        s = UnorderedListStack()
        testsPassed += 1
        print("Test passed: stack created") 
    except:
        print("Test failed: couldn't initialize stack")

    try: 
        s.push("hello")
        s.push(3)
        testsPassed += 1
        print("Test passed: items pushed")
    except:
        print("Test failed: couldn't push onto stack")

    try:
        result = s.peek() 
        if (result == 3):
            testsPassed += 1
            print("Test passed: peeked at item") 
        else:
            print("Test failed: incorrect peek value") 
    except:
        print("Test failed: couldn't peek at stack")

    try:
        result = s.pop()
        if (result == 3):
            testsPassed += 1
            print("Test passed: item popped")
        else:
            print("Test failed: incorrect pop result")
    except:
        print("Test failed: couldn't pop")

    try:
        result = s.is_empty() 
        if (not result):
            testsPassed += 1
            print("Test passed: is_empty returned correct result") 
        else:
            print("Test failed: stack has items, but indicated empty") 
    except:
        print("Test failed: is_empty() method unavailable")

    try:
        result = s.size() 
        if (result == 1):
            testsPassed += 1
            print("Test passed: correct size returned")
        else:
            print("Test failed: incorrect size returned") 
    except:
        print("Test failed: .size() method unavailable")

    try: 
        s.pop()
    except: 
        pass
    
    try:
        result = s.is_empty() 
        if (result):
            testsPassed += 1
            print("Test passed: .is_empty() correctly indicating empty status") 
        else:
            print("Test failed: stack failed to indicate empty status") 
    except:
        print("Test failed: is_empty() unavailable")
    
    print(str(testsPassed) + "/7 tests passed")

if __name__ == "__main__":
    main()
