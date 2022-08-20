import binaryTree as bt

#recursive
def treeValues(node):
    if not(node.val): return False
    print(node.val)
    if node.left :treeValues(node.left)
    if node.right :treeValues(node.right)
    return True

treeValues(bt.a)