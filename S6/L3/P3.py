# Reverse a Linked List (Recursive)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverseLL(head):
    if head is None or head.next is None:
        return head
    temp = reverseLL(head.next)
    front = head.next
    front.next = head
    head.next = None
    return temp

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
head = reverseLL(head)
printLL(head)
