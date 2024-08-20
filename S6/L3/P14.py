# Add 1 to a number represented by Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLL(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

def addOneUntil(head):
    res = head
    temp = None
    carry = 1
    while head is not None:
        sum = carry + head.data
        carry = 1 if sum >= 10 else 0
        sum = sum if sum < 10 else sum % 10
        head.data = sum
        temp = head
        head = head.next
    if carry > 0:
        temp.next = Node(carry)
    return res

def addOne(head):
    head = reverseLL(head)
    head = addOneUntil(head)
    head = reverseLL(head)
    return head

def printLL(head):
    while head is not None:
        print(head.data, end = " -> ")
        head = head.next
    print("None")

head = Node(9)
head.next = Node(9)
head.next.next = Node(9)
head.next.next.next = Node(9)
printLL(head)
head = addOne(head)
printLL(head)
