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

def main():
    print("Testing the UnorderedList class")
    tests_passed = 0
    try:
        ul = UnorderedList()
        tests_passed += 1
        print("Test passed: UnorderedList object created")
    except:
        print("Test failed: couldn't create UnorderedList object")

    try:
        if ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method detected empty list")
        else:
            print("Test failed: .is_empty() method didn't understand that list is empty")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 0:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 0")
        else:
            print("Test failed: .length() didn't identify a length of 0")
    except:
        print("Test failed: .length() method unavailable")
        
    try:
        ul.add(4)
        ul.add(3)
        ul.add(2)
        ul.add(1)
        ul.add(0)
        tests_passed += 1
        print("Test passed: five items added")
    except:
        print("Test failed: couldn't add items")
    
    try:
        if not ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method identified that list is no longer empty")
        else:
            print("Test failed: .is_empty() method thought list was empty, and it isn't")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 5:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 5")
        else:
            print("Test failed: .length() didn't identify a length of 5")
    except:
        print("Test failed: .length() method unusable")
     
    try:
        result = str(ul)         # Try using __repr__
        if result == "UnorderedList[0,1,2,3,4,]":
            tests_passed += 1
            print("Test passed: __repr__ returning correct values:")
            print(result)
        else:
            print("Test failed: __repr__ returned " + result)
            print("Expected: UnorderedList[0,1,2,3,4,]")
        
    except:
        print("Test failed: couldn't reference __repr__ method")
    
    try:
        if not ul.search(5):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 5 isn't on list")
        else:
            print("Test failed: .search() method thought 5 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
        
    try:
        if ul.search(3):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 3 is on list")
        else:
            print("Test failed: .search() method thought 3 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
    
    try:
        ul.remove(0)
        if str(ul) == "UnorderedList[1,2,3,4,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from beginning of list")
        else:
            print("Test failed: .remove() didn't remove item from beginning of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from middle of list")
        else:
            print("Test failed: .remove() didn't remove item from middle of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
        
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(2)
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from end of list")
        else:
            print("Test failed: .remove() didn't remove item from end of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(3)
        if str(ul) == "UnorderedList[0,1,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully didn't remove item from list")
        else:
            print("Test failed: .remove() failed in not removing a non-existent item from list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(0)
        ul.add(1)
        ul.add(0)
        print("Attempting multiple remove")
        print("Before remove: " + str(ul))
        ul.remove(0)
        print("After remove: " + str(ul))
        result = ul.search(0)
        if not result:
            tests_passed += 1
            print("Test passed: .remove() successfully removed multiple items")
        else:
            print("Test failed: .remove() didn't remove multiple items")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.append(3)
        if str(ul) == "UnorderedList[0,1,2,3,]":
            tests_passed += 1
            print("Test passed: .append() successfully appended item to list")
        else:
            print("Test failed: .append() didn't append item to list")
    except:
        print("Test failed: .append() method unavailable or not working?")
    
    try:
        result = ul.index(1)
        if result == 1:
            tests_passed += 1
            print("Test passed: .index() successfully found item on list")
        else:
            print("Test failed: .index() failed to find item on list")
    except:
        print("Test failed: .index() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.insert(0, -1)
        if str(ul) == "UnorderedList[-1,0,1,2,]":
            tests_passed += 1
            print("Test passed: .insert() successfully inserted value at beginning of list")
        else:
            print("Test failed: .insert() didn't correctly insert at beginning of list")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.insert(2,3)
        if str(ul) == "UnorderedList[0,1,3,2,]":
            tests_passed += 1
            print("Test passed: .insert() successfully inserted values in middle of list")
        else:
            print("Test failed: .insert() didn't correctly insert values in middle of list")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop()
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .pop() successfully removed last item from list")
        else:
            print("Test failed: .pop() didn't remove last item from list correctly")
    except:
        print("Test failed: .pop() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(0)
        if str(ul) == "UnorderedList[1,2,]":
            tests_passed += 1
            print("Test passed: .pop(0) successfully removed first item from list")
        else:
            print("Test failed: .pop(0) didn't remove first item from list correctly")
    except:
        print("Test failed: .pop(0) method unavailable? (or __repr__ not working?)")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .pop(1) successfully removed item from middle of list")
        else:
            print("Test failed: .pop(1) didn't remove last item from middle of list correctly")
    except:
        print("Test failed: .pop(1) method unavailable? (or __repr__ not working?)")


        
    print(str(tests_passed) + "/21 tests passed on the UnorderedList class")


if __name__ == "__main__":
    main()
