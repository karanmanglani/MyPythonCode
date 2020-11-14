import math
class Node(object):
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len  = 0

    def push(self,value):
        node = Node(value)
        if(self.len == 0):
             self.head = node
             self.tail = node
        else:
            if(not self.head.next): # If there is no node next to head
                self.head.next = node 
                node.prev = self.head
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

    def pop(self):
        if(self.len > 1):
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
        elif(self.len == 1):
            self.head = self.tail = None
            self.len -= 1
        else:
            return None

    def shift(self):
        if(self.len > 1):
            self.head = self.head.next
            self.head.prev = None
            self.len -= 1
        elif(self.len == 1):
            self.head = self.tail = None
            self.len -= 1

    def unshift(self,val):
        node = Node(val)
        if(not self.head):
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev
        self.len += 1
        return self

    def get(self,index):
        i = 0
        if(index < 0 or index >= self.len):
            return None
        elif(index <= math.floor(self.len/2)):
            current = self.head
            for i in range(index):
                current = current.next
            return current
        else:
            current = self.tail
            for i in range(self.len-1,math.floor(self.len/2) + 1,-1):
                current = current.prev
            return current

    def set(self,index,value):
        current = self.get(index)
        if(current):
            current.value = value
            return True
        else:
            return False


dll = DoublyLinkedList()
dll.push("Hi")
dll.push("I am")
dll.unshift("Karan")

print(dll.get(2).value)
