# Check if Linked List is Palindrome or not
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverseLL(head):
    if head is None or head.next is None:
        return head
    temp = reverseLL(head.next)
    front = head.next
    front.next = head
    head.next = None
    return temp

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    slow = reverseLL(slow)
    while slow:
        if head.data != slow.data:
            return False
        head = head.next
        slow = slow.next
    return True

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(4, Node(3, Node(2, Node(1)))))))))
printLL(head)
print(isPalindrome(head))
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
printLL(head)
print(isPalindrome(head))
