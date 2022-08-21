import queue
import binaryTree as bt

def bredthFirstValues(node):
    if not(node): return []
    queue = [node]
    array = []
    while len(queue)>0:
        current = queue.pop(0)
        array.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)    
    return array

nodes = bredthFirstValues(bt.a)
print(nodes)