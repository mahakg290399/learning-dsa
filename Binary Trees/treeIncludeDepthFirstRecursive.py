from locale import currency
import binaryTree as bt

def treeIncludes(root, target):
    if not(root): return False
    if root.val == target: return True    
    return(treeIncludes(root.left, target) or treeIncludes(root.right, target))
    

print(treeIncludes(bt.a,'f'))