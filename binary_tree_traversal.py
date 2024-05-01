#!/usr/bin/env python3

"""
binary_tree_traversal.py
Creates and fills a binary tree and shows strategies for 
traversing the tree.
"""

__author__ = "Kamryn Chan"
__version__ = "2024-04-11"


from atds import BinaryTree

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def inorder(tree):
  if tree != None:
      inorder(tree.get_left_child())
      print(tree.get_root_val())
      inorder(tree.get_right_child())
    
def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def main():
    bt = BinaryTree("A")
    bt.insert_left("B")
    bt.insert_right("C")
    bt.get_left_child().insert_left("D")
    bt.get_left_child().insert_right("E")
    bt.get_left_child().get_left_child().insert_left("H")
    bt.get_left_child().get_left_child().insert_right("I")
    bt.get_left_child().get_right_child().insert_left("J")
    bt.get_right_child().insert_left("F")
    bt.get_right_child().insert_right("G")
    bt.get_right_child().get_right_child().insert_left("K")
    print("Preorder: ")
    preorder(bt)
    print("Inorder: ")
    inorder(bt)
    print("Postorder: ")
    postorder(bt)


if __name__ == "__main__":
    main()