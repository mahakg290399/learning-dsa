from os import curdir
import queue
import binaryTree as bt

def treeIncludes(root, target):
    if root == None: return False
    queue = [root]
    while(len(queue)>0):
        current = queue.pop(0)
        print(current.val)
        if current.val == target: return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False

print(treeIncludes(bt.a,'b'))