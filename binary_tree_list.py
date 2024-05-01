#!/usr/bin/env python3

"""
binary_tree_list.py
This program implements a list-based representation of a Binary Tree.
"""

__author__ = "Kamryn Chan"
__version__ = "2024-04-03"

def binary_tree(val):
    return [val, [], []]

def get_root_val(node):
    return node[0]

def set_root_val(node, new_val):
    node[0] = new_val

def get_left_child(node):
    return node[1]

def get_right_child(node):
    return node[2]

def insert_left(node, new_branch):
    new_left = binary_tree(new_branch)
    new_left[1] = node[1]
    node[1] = new_left

def insert_right(node, new_branch):
    new_right = binary_tree(new_branch)
    new_right[2] = node[2]
    node[2] = new_right

def main():
    t = binary_tree(3)
    print("Instruction: t = binary_tree(3)")
    print("Result:", t)
    print("Expect: [3, [], []]")
    insert_left(t, 4)
    print("Instruction: insert_left(t, 4)")
    print("Result:", t)
    print("Expect: [3, [4, [], []], []]")
    insert_left(t, 5)
    print("Instruction: insert_left(t, 5)")
    print("Result:", t)
    print("Expect: [3, [5, [4, [], []], []], []]")
    insert_right(t, 6)
    print("Instruction: insert_right(t, 6)")
    print("Result:", t)
    print("Expect: [3, [5, [4, [], []], []], [6, [], []]]")
    insert_right(t, 7)
    print("Instruction: insert_right(t, 7)")
    print("Result:", t) 
    print("Expect: [3, [5, [4, [], []], []], [7, [], [6, [], []]]]")
    l = get_left_child(t)
    print("Instruction: l = get_left_child(t)")
    print("Result: l =", l)
    print("Expect: l = [5, [4, [], []], []]")
    set_root_val(l, 9)
    print("Instruction: set_root_val(l, 9)")
    print("Result: l =", l)
    print("Expect: l = [9, [4, [], []], []]")
    insert_left(l, 11)
    print("Instruction: insert_left(l, 11)")
    print("Result:", t)
    print("Expect: [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]")
    print("Instruction: print(get_right_child(get_right_child(t)))")
    print("Result:", get_right_child(get_right_child(t)))
    print("Expect: [6, [], []]")    
    
if __name__ == "__main__":
    main()
