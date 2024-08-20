# Remove Duplicates from Doubly Linked List
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def insertAtEnd(head, data):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = Node(data, None, temp)

def removeDuplicates(head):
    temp = head
    while temp is not None:
        if temp.next is not None and temp.data == temp.next.data:
            temp.next = temp.next.next
            if temp.next is not None:
                temp.next.prev = temp
        else:
            temp = temp.next
    return head

def printList(head):
    print('None', end=' <-> ')
    while head is not None:
        print(head.data, end=' <-> ')
        head = head.next
    print('None')

head = Node(1)
insertAtEnd(head, 1)
insertAtEnd(head, 2)
insertAtEnd(head, 2)
insertAtEnd(head, 3)
insertAtEnd(head, 3)
insertAtEnd(head, 3)
insertAtEnd(head, 4)
printList(head)
head = removeDuplicates(head)
printList(head)
