#!/usr/bin/env/ python3
"""
create_this_tree.py
Write a main program to create each of the trees given here.
This program prints out expected results based on a __str__() or __repr__() method 
being availabe for the BinaryTree class.
"""

from atds import BinaryTree

def main():
    print('''
    bt1:
                           A
                         /   \\
                        B     C
                      /
                     D
        ''')
    print('''Expected result, bt1:
    BinaryTree[key=A,
    left_child=BinaryTree[key=B,
    left_child=BinaryTree[key=D,
    left_child=None,
    right_child=None],
    right_child=None],
    right_child=BinaryTree[key=C,
    left_child=None,
    right_child=None]]''')
    print('--------------------')
    print("Example Solution")
    print('My result:')
    bt1 = BinaryTree('A')
    bt1.insert_right('C')
    bt1.insert_left('D')
    bt1.insert_left('B')
    print(bt1)
    print('--------------------')
    # Another way of doing the same tree
    bt1a = BinaryTree('A')
    bt1a.insert_left('B')
    bt1a.get_left_child().insert_left('D')
    bt1a.insert_right('C')
    print(bt1a)
    print('--------------------')
    print('''
    bt2:
                            A
                          /   \\
                         /     \\
                        B       C
                         \\     / \\
                          D   E   F
    ''')
    print('''Expected result bt2:
    BinaryTree[key=A,
    left_child=BinaryTree[key=B,
    left_child=None,
    right_child=BinaryTree[key=D,
    left_child=None,
    right_child=None]],
    right_child=BinaryTree[key=C,
    left_child=BinaryTree[key=E,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=F,
    left_child=None,
    right_child=None]]]''')
    print('--------------------')
    print('My result:')
    bt2 = BinaryTree("A")
    bt2.insert_left("B")
    bt2.insert_right("C")
    bt2.get_left_child().insert_right("D")
    bt2.get_right_child().insert_left("E")
    bt2.get_right_child().insert_right("F")
    print(bt2)











    print('--------------------')
    print('''
    bt3:
                            A
                              \\
                                B
                               / 
                             C
                            / \\ 
                          D    E
    ''')

    print('''Expected result bt3:
    BinaryTree[key=A,
    left_child=None,
    right_child=BinaryTree[key=B,
    left_child=BinaryTree[key=C,
    left_child=BinaryTree[key=D,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=E,
    left_child=None,
    right_child=None]],
    right_child=None]]''')
    print('--------------------')
    print('My result:')
    bt3 = BinaryTree("A")
    bt3.insert_right("B")
    bt3.get_right_child().insert_left("C")
    bt3.get_right_child().get_left_child().insert_left("D")
    bt3.get_right_child().get_left_child().insert_right("E")
    print(bt3)










    print('--------------------')
    print('''
    bt4:
                            A
                          /   \\
                        /       \\
                      /           \\
                    B               C
                  /   \\           /   \\
                /       \\       /       \\
              D           E   F           G
            /   \\       /
           H      I    J
    ''')

    print('''Expected result bt4:
    BinaryTree[key=A,
    left_child=BinaryTree[key=B,
    left_child=BinaryTree[key=D,
    left_child=BinaryTree[key=H,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=I,
    left_child=None,
    right_child=None]],
    right_child=BinaryTree[key=E,
    left_child=BinaryTree[key=J,
    left_child=None,
    right_child=None],
    right_child=None]],
    right_child=BinaryTree[key=C,
    left_child=BinaryTree[key=F,
    left_child=None,
    right_child=None],
    right_child=BinaryTree[key=G,
    left_child=None,
    right_child=None]]]''')
    print('--------------------')
    print('My result:')
    bt4 = BinaryTree("A")
    bt4.insert_left("B")
    bt4.insert_right("C")
    bt4.get_left_child().insert_left("D")
    bt4.get_left_child().insert_right("E")
    bt4.get_left_child().get_left_child().insert_left("H")
    bt4.get_left_child().get_left_child().insert_right("I")
    bt4.get_left_child().get_right_child().insert_left("J")
    bt4.get_right_child().insert_left("F")
    bt4.get_right_child().insert_right("G")
    print(bt4)
    
    
    
    
    
    
    
    
    
    
    
    print('--------------------')
    


main()


