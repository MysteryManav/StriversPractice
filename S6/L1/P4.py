# Find the length of the linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printLL(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def lengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
printLL(head)
print(lengthLL(head))
