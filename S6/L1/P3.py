# Deleting a Node in LinkedList
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def printLL(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def deleteTail(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
printLL(head)
head = deleteTail(head)
head = deleteTail(head)
printLL(head)
