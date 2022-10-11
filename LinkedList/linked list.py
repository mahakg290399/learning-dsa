from node import Node
class linkedList(Node):

    firstNode = Node()
    lastNode = Node()
    firstNode.next=lastNode
    
    def addFirst(self,val):
        self.firstNode = Node(val,self.firstNode)
    
    
    def addLast(self,val):
        self.lastNode = Node(val,self.lastNode)
    
    def printAll(self):
        print("self",self.val)
        temp = self
        while temp.next:
            print(temp.val)
            temp = temp.next
    
    def deleteFirst(self):
        self.firstNode = self.firstNode.next

    def deleteLast(self):
        cursor = self.firstNode
        cursorNext = self.firstNode.next
        while cursorNext.next:
            cursor, cursorNext = cursorNext.val, cursorNext.next
        self.lastNode=cursor

    def buildLL(self,liss):
        self.lastNode.next = None
        self.lastNode.val = Node(liss[0])
        prevNode = self.lastNode
        for val in liss[::-1]:
            firsNode = Node(val)
            firsNode.next = prevNode
            self.firstNode = firsNode      
        return self.firstNode


