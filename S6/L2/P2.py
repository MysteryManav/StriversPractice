# Insert at end of Doubly Linked List
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def printLL(head):
    print("None <-> ", end="")
    while head is not None:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

def insertEnd(head, data):
    if head is None:
        return Node(data)
    temp = head
    newNode = Node(data)
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp
    return head

head = None
head = insertEnd(head, 1)
head = insertEnd(head, 2)
head = insertEnd(head, 3)
head = insertEnd(head, 4)
printLL(head)
