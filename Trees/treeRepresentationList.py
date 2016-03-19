__author__ = 'bhushan'
from pprint import pprint

# List of list representation

my_tree = ['A', # Root
           ['B',# Left subtree
            ['D', [], []],
            ['E', [], []] ],
           ['C', # Right subtree
            ['F',[], []],
            [] ]
]

print("Root " + my_tree[0] + "\n") # gives root node
print("Left Subtree", my_tree[1])  # Gives left subtree
print("\n")
print("Right Subtree", my_tree[2]) # Gives right subtree
print("\n")