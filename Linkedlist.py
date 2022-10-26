'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

        def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node  

'''

#Create nodes
from dataclasses import dataclass
from email import header
from sys import last_traceback


class Node:
   def __init__(self, data):
        self.data = data
        self.next = None


#Create  linked list
class LinkedList:
    def __init__(self):
        self.head = None

# Add nodes to Linked List
    #Node => data, next
    #firstNode.data => John, firstNode.next => None
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


llist = LinkedList()

firstNode = Node("John")
llist.insert(firstNode)

secondNode = Node("Ben")
llist.insert(secondNode)

thirdNode = Node("Jerry")
llist.insert(thirdNode)
#Print Linked List

