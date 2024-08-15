# Delete the last Node in Linked List
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def printLL(head):
    print("None <-> ", end="")
    while head is not None:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

def deleteEnd(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.prev.next = None
    temp.prev = None
    del temp
    return head

head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
printLL(head)
head = deleteEnd(head)
printLL(head)
