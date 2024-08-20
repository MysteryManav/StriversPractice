# Sort Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.data < right.data:
        left.next = merge(left.next, right)
        return left
    else:
        right.next = merge(left, right.next)
        return right
    
def mergeSort(head):
    if head is None or head.next is None:
        return head
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    left = mergeSort(head)
    right = mergeSort(slow)
    return merge(left, right)

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(8, Node(7, Node(6))))))))
printLL(head)
head = mergeSort(head)
printLL(head)
