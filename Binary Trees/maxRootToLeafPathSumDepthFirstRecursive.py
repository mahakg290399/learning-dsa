from turtle import right
import binaryTree as bt
from math import inf

def maxRootToLeafPath(root):
    if not(root): return -inf
    if not(root.left) and not(root.right): return root.val
    leftValue = maxRootToLeafPath(root.left)
    rightValue = maxRootToLeafPath(root.right)
    maxChild = max(leftValue, rightValue)
    return root.val+maxChild

print(maxRootToLeafPath(bt.nodeA))