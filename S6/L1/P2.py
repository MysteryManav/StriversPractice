# Insert a node in Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printLL(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def insertHead(head, data):
    temp = Node(data, head)
    return temp

head = Node(1)
head = insertHead(head, 2)
head = insertHead(head, 3)
head = insertHead(head, 4)
printLL(head)
