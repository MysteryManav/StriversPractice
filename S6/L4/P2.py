# Find pairs with given sum in Doubly Linked List
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

def findPairs(head, sum):
    first = head
    last = head
    pairs = []
    while last.next is not None:
        last = last.next
    while first is not None and last is not None:
        if first.data == last.data:
            break
        elif first.data > sum:
            break
        elif last.data > sum:
            last = last.prev
        elif first.data + last.data < sum:
            first = first.next
        elif first.data + last.data > sum:
            last = last.prev
        else:
            pairs.append((first.data, last.data))
            first = first.next
            last = last.prev
    return pairs

def printList(head):
    print('None', end=' <-> ')
    while head is not None:
        print(head.data, end=' <-> ')
        head = head.next
    print('None')

head = Node(1)
insertAtEnd(head, 2)
insertAtEnd(head, 3)
insertAtEnd(head, 4)
insertAtEnd(head, 5)
insertAtEnd(head, 6)
insertAtEnd(head, 7)
insertAtEnd(head, 8)
insertAtEnd(head, 9)
insertAtEnd(head, 10)
printList(head)
print(findPairs(head, 0))
print(findPairs(head, 5))
print(findPairs(head, 10))
print(findPairs(head, 15))
print(findPairs(head, 20))
print(findPairs(head, 25))
print(findPairs(head, 30))
