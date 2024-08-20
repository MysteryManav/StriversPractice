# Find middle element of a Linked List: Tortoise Hare Method
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

def findMiddle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
print(findMiddle(head))
