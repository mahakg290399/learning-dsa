import binaryTree as bt

def treeSum(root):
    if not(root): return 0
    return (root.val+ treeSum(root.left) + treeSum(root.right))

print(treeSum(bt.nodeA)) 