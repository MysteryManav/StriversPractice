# Reverse a Doubly Linked List
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

def reverseLL(head):
    if head is None or head.next is None:
        return head
    temp = None
    current = head
    while current is not None:
        temp = current.prev 
        current.prev = current.next
        current.next = temp
        current = current.prev
    return temp.prev

head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
printLL(head)
head = reverseLL(head)
printLL(head)
