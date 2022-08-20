import queue
import binaryTree as bt

def bredthFirstValues(node):
    if not(node): return []
    queue = [node]
    array = []
    while len(queue)>0:
        current = queue.pop(0)
        array.append(current.val)
        if current.right: queue.append(current.right)
        if current.left: queue.append(current.left)
        
    return array

nodes = bredthFirstValues(bt.a)
print(nodes)