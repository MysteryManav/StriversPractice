# Reverse a Linked List (Iterative)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverseLL(head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
head = reverseLL(head)
printLL(head)
