# Segeregate Even and Odd nodes in Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def segeregate_even_and_odd(head):
    if head is None or head.next is None:
        return head
    even_head = even = None
    odd_head = odd = None
    while head:
        if head.data % 2 == 0:
            if even is None:
                even_head = even = head
            else:
                even.next = head
                even = even.next
        else:
            if odd is None:
                odd_head = odd = head
            else:
                odd.next = head
                odd = odd.next
        head = head.next
    if even:
        even.next = odd_head
    if odd:
        odd.next = None

    return even_head

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
head = segeregate_even_and_odd(head)
printLL(head)
