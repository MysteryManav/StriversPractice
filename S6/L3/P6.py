# Length of Loop in Linked List
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

def findLoopLength(head):
    if head is None:
        return 0
    slow = detectLoop(head)
    if slow is None:
        return 0
    length = 1
    fast = slow.next
    while slow != fast:
        fast = fast.next
        length += 1
    return length

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
print(findLoopLength(head))
head.next.next.next.next.next.next.next.next = head.next.next.next
print(findLoopLength(head))
