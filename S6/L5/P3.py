# Flattening a Linked List
class Node:
    def __init__(self, data, next=None, child=None):
        self.data = data
        self.next = next
        self.child = child

def merge(list1, list2):
    temp = Node(-1)
    result = temp
    while list1 and list2:
        if list1.data < list2.data:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next
    if list1:
        result.next = list1
    else:
        result.next = list2
    
    if temp.child:
        temp.child.next = None
    return temp.child

def flattenLinkedList(head):
    if not head or not head.next:
        return head
    
    mergeHead = flattenLinkedList(head.next)
    head = merge(head, mergeHead)
    return head

def printList(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print()

def printOriginalList(head):
    while head:
        print(head.data, end=' -> ')
        if head.child:
            print('(', end=' ')
            printOriginalList(head.child)
            print(')', end=' ')
        head = head.next
    print()

head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

print('Original List:')
printOriginalList(head)
head = flattenLinkedList(head)
print('Flattened List:')
printList(head)
