# Add 2 numbers in Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

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

def addTwoNumbers(l1, l2):
    l1 = reverseLL(l1)
    l2 = reverseLL(l2)
    res = None
    temp = None
    carry = 0
    while l1 is not None and l2 is not None:
        sum = l1.data + l2.data + carry
        carry = 1 if sum >= 10 else 0
        sum = sum if sum < 10 else sum % 10
        if res is None:
            res = Node(sum)
            temp = res
        else:
            temp.next = Node(sum)
            temp = temp.next
        l1 = l1.next
        l2 = l2.next
    while l1 is not None:
        if carry > 0:
            sum = l1.data + carry
            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10
            temp.next = Node(sum)
            temp = temp.next
            l1 = l1.next
        else:
            temp.next = Node(l1.data)
            temp = temp.next
            l1 = l1.next
    while l2 is not None:
        if carry > 0:
            sum = l2.data + carry
            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10
            temp.next = Node(sum)
            temp = temp.next
            l2 = l2.next
        else:
            temp.next = Node(l2.data)
            temp = temp.next
            l2 = l2.next
    if l1 is None and l2 is None:
        if carry > 0:
            temp.next = Node(carry)
            temp = temp.next
    res = reverseLL(res)
    return res

def printLL(head):
    while head is not None:
        print(head.data, end = " -> ")
        head = head.next
    print("None")

l1 = Node(9)
l1.next = Node(9)
l1.next.next = Node(9)
l1.next.next.next = Node(9)
l1.next.next.next.next = Node(9)
l1.next.next.next.next.next = Node(9)
l1.next.next.next.next.next.next = Node(9)
l2 = Node(9)
l2.next = Node(9)
l2.next.next = Node(9)
l2.next.next.next = Node(9)
printLL(l1)
printLL(l2)
res = addTwoNumbers(l1, l2)
printLL(res)
