class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self,value):

        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self 
    
    def pop(self):
        if(self.length > 0):
            current = self.head
            while(current.next.next):
                current = current.next
            current.next = None
            self.tail = current
            self.length -= 1
        elif(self.length == 0):
            self.tail ,self.head = None
            return self
        else:
            return None

    def shift(self):
        if(self.length > 0):
            current = self.head
            self.head = current.next
            current = None 
            self.length -= 1
            if(self.length == 0 ):
                self.head , self.tail = None
            return self
        else:
            return None

    def unshift(self,val):
        newHead = Node(val)
        if(not self.head):
            self.head = newHead
            self.tail = self.head
        else:    
            newHead.next = self.head
            self.head = newHead
        self.length += 1
        return self

    def get(self,n):
        if self.length < 1:
            return None
        current = self.head
        for i in range(n):
            current = current.next 
        return current
    
    def set(self,val,index):
        current = self.get(index)
        if(current):
            current.val = val
            return True
        else:
            return False

    def insert(self,index,value):
        newNode = Node(value)
        if(index < 0 or index > self.length):
            return False
        elif(index == self.length):
            self.push(value)
        elif(index == 0):
            self.unshift(value)
        else:
            prev = self.get(index)
            self.get(index - 1).next = newNode
            newNode.next = prev
            self.length += 1
        return True

    def remove(self, index):
        if(index < 0 or index >= self.length):
            return None
        elif(index == self.length - 1):
            self.pop()
        elif(index == 0):
            self.shift()
        else:
            new = self.get(index - 1)
            new.next = new.next.next
        self.length -= 1
        return None
        
    def reverse(self):
        # Swapping head and tail
        currentNode = self.head
        self.head = self.tail
        self.tail = currentNode

        # looping through list
        prev = next = None 
        for i in range(0,self.length):
            next = currentNode.next 
            currentNode.next = prev 
            prev = currentNode
            currentNode = next
        return self

    def printAllValues(self):
        for i in range(0,self.length):
            print(sll.get(i).val)


sll = SinglyLinkedList()
sll.push("Hello")
sll.push("There")
sll.push("I'm Karan")
sll.shift()
print(sll.head.val)