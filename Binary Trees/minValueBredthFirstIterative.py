from cgitb import small
import queue
import binaryTree as bt
from math import inf

def minValue(root):
    if not(root): return inf
    queue = [root]
    smallest = inf
    while len(queue)>0:
        current = queue.pop(0)
        if current.val<smallest: smallest=current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return smallest
print(minValue(bt.nodeA))