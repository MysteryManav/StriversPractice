# Find the starting point in Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def detectLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None

def findStart(head):
    if head is None:
        return None
    slow = head
    fast = detectLoop(head)
    if fast is None:
        return None
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.data

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
print(findStart(head))
head.next.next.next.next.next.next.next.next = head.next.next.next
print(findStart(head))
