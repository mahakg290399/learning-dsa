from math import inf
import binaryTree as bt

def minValue(root):
    if not(root): return inf
    return min(root.val,minValue(root.left),minValue(root.right))

print(minValue(bt.nodeA))



