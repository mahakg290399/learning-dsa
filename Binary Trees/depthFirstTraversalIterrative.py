from locale import currency
import binaryTree as bt

def treeValues(node):
    if not(node) : return False
    if node.val == None: return False
    stack=[node]
    
    while(len(stack)>0):
        current = stack.pop()
        if current.right : stack.append(current.right)
        if current.left : stack.append(current.left)
        print(current.val)




treeValues(bt.a)
