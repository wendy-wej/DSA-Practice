class Node:
    def __init__(self,val,n=None):
        self.val = val
        self.next = n


node1 = Node (10)
node2 = Node (4)
node3 = Node (1)
node4 = Node (16)

node1.next = node2
node2.next = node3
node3.next = node4

dummy = Node(-500,node1)
s = node1
c = node1.next

while(c):

    if( s.val <c.val):
        s = s.next
        c = c.next
        
    else:
        t = dummy

        while(t.next.val < c.val):
            t = t.next

        s.next = c.next
        c.next = t.next
        t.next = c
        c = s.next

print(dummy.value) # this prints the sorted linked list
print(Node)