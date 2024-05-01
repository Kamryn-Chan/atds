#!/usr/bin/env python3

"""
program_name.py
This is a template for a Python program.
"""

__author__ = "Kamryn Chan"
__version__ = "2024-04-11"

from atds import Stack,BinaryTree

def build_parse_tree(fpexpr):
    tokens = fpexpr.split()
    # print(tokens)
    bt = BinaryTree(None)
    st = Stack()
    focus = bt
    for token in tokens:
        print("Examining",token)
        if token == "(":
            left_child = BinaryTree(None)
            focus.insert_left(left_child)
            st.push(focus)
        elif token in ('+','-','*','/','**'):
            focus.set_root_vale(token)
            right_child = BinaryTree(None)
            focus.insert_right(right_child)
            st.push(focus)
            focus = focus.get_right_child
        elif token == ')':
            focus = st.pop()
        else:           # must be an opperand
            focus.set_root_val(token)
            focus = st.pop()
        print(focus)
        input()

    print("Done with binary tree creation")
    print(bt)
    print()
    return bt

def evaluate(parse_tree): 
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()
    if left == None and right == None:
        return float(parse_tree.get_root_value())
    else:
        sign = parse_tree.get_root_value()
        if sign == "+":
            return evaluate(left) + evaluate(right)
        elif sign == '*':
            return evaluate(left) * evaluate(right)

def main():
    # The program goes here
    fpexpr = '( 2 + ( 3 * 7 ) )'
    parse_tree = build_parse_tree(fpexpr)



if __name__ == "__main__":
    main()