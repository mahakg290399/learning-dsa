from os import curdir
import queue
import binaryTree as bt

def treeSum(root):
    if not(root): return False
    sum = 0
    queue = [root]
    while len(queue)>0:
        current = queue.pop(0)
        sum += current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return sum

print(treeSum(bt.nodeA))