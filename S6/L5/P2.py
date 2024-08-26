# Rotate a Linked List to the right by K places
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

def rotateLL(head, k):
    if head is None or head.next is None:
        return head
    for i in range(k):
        temp = head
        while temp.next.next is not None:
            temp = temp.next
        end = temp.next
        temp.next = None
        end.next = head
        head = end
    return head

def printLL(head):
    print("None", end=" <-> ")
    while head is not None:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

def insertAtEnd(head, data):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = Node(data)
    return head

head = Node(1)
head = insertAtEnd(head, 2)
head = insertAtEnd(head, 3)
head = insertAtEnd(head, 4)
head = insertAtEnd(head, 5)
head = insertAtEnd(head, 6)
head = insertAtEnd(head, 7)
printLL(head)
head = rotateLL(head, 3)
printLL(head)
