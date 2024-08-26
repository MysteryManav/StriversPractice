# Clone Linked List with a Random Pointer and a Next Pointer
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insertCopyInBetween(head):
    temp = head
    while temp:
        nextElement = temp.next
        copy = Node(temp.data)
        copy.next = nextElement
        temp.next = copy
        temp = nextElement

def connectRandomPointers(head):
    temp = head
    while temp:
        copy = temp.next
        if temp.random:
            copy.random = temp.random.next
        else:
            copy.random = None
        temp = temp.next.next

def getDeepCopyList(head):
    temp = head
    dummyNode = Node(-1)
    res = dummyNode
    while temp:
        res.next = temp.next
        res = res.next
        temp.next = temp.next.next
        temp = temp.next
    return dummyNode.next

def cloneLinkedList(head):
    if not head:
        return None
    insertCopyInBetween(head)
    connectRandomPointers(head)
    return getDeepCopyList(head)

def printList(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next.next.next
head.next.next.next.next.random = head.next
printList(head)
copy = cloneLinkedList(head)
printList(copy)
