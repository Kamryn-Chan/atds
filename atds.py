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

    def __repr__(self):
        return str(self.ul)

class HashTable():
    """Describes a hash table that will store key-value pairs.
    """
    def __init__(self, m):
        """Creates an empty hash table of size m.
        """
        self.size = m
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        """Creates an entry in the hash table.
        """
        hash_value = key % self.size
        while self.slots[hash_value] != None:
            hash_value += 1
        if self.slots[hash_value] == key:
            self.data[hash_value] = value
        else:
            self.slots[hash_value] = key
            self.data[hash_value] = value

    def get(self, key):
        """Returns the value associated with the key or None.
        """
        hash_value = key % self.size
        if self.slots[hash_value] == key:
            return self.data[hash_value]
        else:
            while self.slots[hash_value] != None:
                if self.slots[hash_value] == key:
                    return self.data[hash_value]
                hash_value += 1
        return None

    def __repr__(self):
        """Returns a String representation of the hash table.
        """
        return "Keys:   " + str(self.slots) + "\n" + "Values: " + str(self.data)

class BinaryTree(object):
    """Constructs a binary tree.
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_root_val(self):
        return self.val

    def set_root_val(self, new_val):
        self.val = new_val
    
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def insert_left(self, val):
        new_left = BinaryTree(val)
        new_left.left = self.left
        self.left = new_left

    def insert_right(self, val):
        new_right = BinaryTree(val)
        new_right.right = self.right
        self.right = new_right

    def __str__(self):
        return "BinaryTree[key=" + str(self.val) + ", left_child=" + str(self.left) + ", right_child=" + str(self.right) + "]"

def main():
    print("Testing the binary_tree_class file!")
    bt = BinaryTree(3)
    print("Instruction: bt = BinaryTree(3)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=None,right_child=None]")
    print()
    bt.insert_left(4)
    print("Instruction: bt.insert_left(4)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    bt.insert_left(5)
    print("Instruction: bt.insert_left(5)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=None]")
    print()
    bt.insert_right(6)
    print("Instruction: bt.insert_right(6)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=6,left_child=None,right_child=None]]")
    print()
    bt.insert_right(7)
    print("Instruction: bt.insert_right(7)")
    print("Result:", bt) 
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=7,left_child=None,right_child=BinaryTree[key=6,left_child=None,right_child=None]]]")
    print()
    l = bt.get_left_child()
    print("Instruction: l = bt.get_left_child()")
    print("Result: l =", l)
    print("Expect: l = BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    l.set_root_val(9)
    print("Instruction: l.set_root_val(9)")
    print("Result: l =", l)
    print("Expect: l = BinaryTree[key=9,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    l.insert_left(11)
    print("Instruction: l.insert_left(11)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=9,left_child=BinaryTree[key=11,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=None],right_child=BinaryTree[key=7,left_child=None,right_child=BinaryTree[key=6,left_child=None,right_child=None]]]")
    print()
    print("Instruction: print(bt.get_right_child().get_right_child())")
    print("Result:", bt.get_right_child().get_right_child())
    print("Expect: BinaryTree[key=6,left_child=None,right_child=None]")


if __name__ == "__main__":
    main()
