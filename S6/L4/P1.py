# Delete all occurences of a key in Doubly Linked List
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

def deleteAllOccurences(head, key):
    temp = head
    while temp is not None:
        if temp.data == key:
            if temp.prev is None:
                head = temp.next
            else:
                temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
        temp = temp.next
    return head

def printList(head):
    print('None', end=' <-> ')
    while head is not None:
        print(head.data, end=' <-> ')
        head = head.next
    print('None')

head = Node(1)
insertAtEnd(head, 2)
insertAtEnd(head, 3)
insertAtEnd(head, 2)
insertAtEnd(head, 4)
insertAtEnd(head, 2)
insertAtEnd(head, 5)
insertAtEnd(head, 2)
insertAtEnd(head, 6)
insertAtEnd(head, 7)
insertAtEnd(head, 2)
insertAtEnd(head, 8)
insertAtEnd(head, 2)
insertAtEnd(head, 9)
insertAtEnd(head, 2)
insertAtEnd(head, 10)
printList(head)
head = deleteAllOccurences(head, 2)
printList(head)
head = deleteAllOccurences(head, 1)
printList(head)
head = deleteAllOccurences(head, 10)
printList(head)
