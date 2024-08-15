# Search an element in Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printLL(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def searchLL(head, val):
    while head is not None:
        if head.data == val:
            return True
        head = head.next
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
printLL(head)
print(searchLL(head, val=3))
print(searchLL(head, val=5))
