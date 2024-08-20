# Remove N-th Node from back of a Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def removeNthFromEnd(head, n):
    if head is None:
        return head
    dummy = Node(0)
    dummy.next = head
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
head = removeNthFromEnd(head, n=3)
printLL(head)
