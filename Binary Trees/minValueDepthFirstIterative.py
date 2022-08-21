from math import inf
import binaryTree as bt

def minValue(root):
    if not(root): return inf
    smallest = inf
    stack = [root]
    while len(stack)>0:
        current = stack.pop(0)
        if current.val < smallest : smallest = current.val
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return smallest

print(minValue(bt.nodeA))
