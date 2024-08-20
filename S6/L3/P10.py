# Delete the Middle Node of Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def deleteMiddleNode(head):
    if head is None or head.next is None:
        return head
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    temp = slow
    prev.next = slow.next
    del temp
    return head

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, )))))))
printLL(head)
head = deleteMiddleNode(head)
printLL(head)
