# Reverse Linked List in group of given size K
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

def reverseLL(head):
    prev = None
    temp = head
    while temp is not None:
        nextTemp = temp.next
        temp.next = prev
        prev = temp
        temp = nextTemp
    return prev

def getKthNode(temp, k):
    k -= 1
    while temp is not None and k > 0:
        temp = temp.next
        k -= 1
    return temp

def reverseKGroup(head, k):
    temp = head
    prevLast = None
    while temp is not None:
        kthNode = getKthNode(temp, k)
        if kthNode is None:
            if prevLast is not None:
                prevLast.next = temp
            break
        nextTemp = kthNode.next
        kthNode.next = None
        reverseLL(temp)
        if temp == head:
            head = kthNode
        else:
            prevLast.next = kthNode
        prevLast = temp
        temp = nextTemp
    return head

def printLL(head):
    print("None", end=" <-> ")
    while head is not None:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

def insertAtEnd(head, data):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = Node(data)
    return head

head = Node(1)
head = insertAtEnd(head, 2)
head = insertAtEnd(head, 3)
head = insertAtEnd(head, 4)
head = insertAtEnd(head, 5)
head = insertAtEnd(head, 6)
head = insertAtEnd(head, 7)
head = insertAtEnd(head, 8)
head = insertAtEnd(head, 9)
head = insertAtEnd(head, 10)
printLL(head)
head = reverseKGroup(head, 3)
printLL(head)
