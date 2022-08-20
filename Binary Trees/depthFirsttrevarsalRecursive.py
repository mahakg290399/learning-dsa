import binaryTree as bt

#recursive

def treeValues(node):
    # if not(node.val): return False
    # print(node.val)
    # if node.left :treeValues(node.left)
    # if node.right :treeValues(node.right)
    # return True
    if node == None: return []
    leftValues = treeValues(node.left)
    rightValues = treeValues(node.right)
    return [node.val, *leftValues, *rightValues]

print(treeValues(bt.a))