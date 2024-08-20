# Sort a Linked List of 0's, 1's and 2's
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sort012(head):
    if head is None or head.next is None:
        return head
    zero = zero_head = Node(0)
    one = one_head = Node(0)
    two = two_head = Node(0)
    while head:
        if head.data == 0:
            zero.next = head
            zero = zero.next
        elif head.data == 1:
            one.next = head
            one = one.next
        else:
            two.next = head
            two = two.next
        head = head.next
    zero.next = one_head.next
    one.next = two_head.next
    two.next = None
    return zero_head.next

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(0, Node(2, Node(1, Node(0, Node(2, Node(1, Node(0))))))))
printLL(head)
head = sort012(head)
printLL(head)
