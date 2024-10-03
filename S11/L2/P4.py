# Merge M Sorted Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertLinkedList(head, data):
    if head is None:
        head = Node(data)
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
    return head

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end = " ")
        temp = temp.next
    print()

def mergeTwoLinkedList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        head1.next = mergeTwoLinkedList(head1.next, head2)
        return head1
    else:
        head2.next = mergeTwoLinkedList(head1, head2.next)
        return head2

def mergeKSortedList(ll):
    n = len(ll)
    if n == 0:
        return None
    if n == 1:
        return ll[0]
    if n == 2:
        return mergeTwoLinkedList(ll[0], ll[1])
    mid = n // 2
    left = mergeKSortedList(ll[:mid])
    right = mergeKSortedList(ll[mid:])
    return mergeTwoLinkedList(left, right)

ll1 = None
ll1 = insertLinkedList(ll1, 1)
ll1 = insertLinkedList(ll1, 3)
ll1 = insertLinkedList(ll1, 5)
ll2 = None
ll2 = insertLinkedList(ll2, 2)
ll2 = insertLinkedList(ll2, 4)
ll2 = insertLinkedList(ll2, 6)
ll3 = None
ll3 = insertLinkedList(ll3, 0)
ll3 = insertLinkedList(ll3, 9)

ll = [ll1, ll2, ll3]
result = mergeKSortedList(ll)
printLinkedList(result)
