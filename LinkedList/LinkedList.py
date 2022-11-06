import node as n
class LinkedList:
    first = None
    last = None

    def addlast(self,val):
        node = n.Node(val)
        if not self.first: self.first = self.last = node
        else: 
            self.last.next = node 
            self.last = node
    
    def addFirst(self,val):
        node = n.Node(val)
        if not self.first: self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

    def indexof(self,val):
        current = self.first
        count = 1
        while current:
            if current.val == val:
                return count
            current = current.next
            count +=1
        return -1
    
    def contains(self, val):
        current = self.first
        while current:
            if current.val == val : return True
            current = current.next 
        return False

    def removeFirst(self):
        self.first = self.first.next

    def removeLast(self):
        prev = None
        current = self.first
        while current:
            if self.last == current.next : 
                prev = current
                break
            current=current.next
        self.last = prev
        self.last.next = None
        
    def printll(self):
        current = self.first
        while current:
            print(current.val)
            current = current.next

    def sizell(self):
        count = 0
        if not self.first : return count
        current = self.first
        while current:
            current = current.next
            count+=1
        return count

    def toArray(self):
        result = []
        current = self.first
        while current:
            result.append(current.val)
            current = current.next
        return result
        

ll = LinkedList()
ll.addlast(10)
ll.addlast(20)
ll.addlast(30)
ll.addlast(40)
ll.addlast(50)
print(ll.toArray())