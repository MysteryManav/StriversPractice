# Find intersection of two Linked Lists
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def intersectionLL(head1, head2):
    if head1 is None or head2 is None:
        return None
    temp1 = head1
    temp2 = head2
    while temp1 != temp2:
        temp1 = head2 if temp1 is None else temp1.next
        temp2 = head1 if temp2 is None else temp2.next
    return temp1

def printLL(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print("None")

head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
head2 = Node(11, Node(12, Node(13, Node(14, Node(15, Node(16, Node(17, Node(18))))))))
temp = head2
while temp.next:
    temp = temp.next
temp.next = head1.next.next.next
printLL(head1)
printLL(head2)
inter = intersectionLL(head1, head2)
while inter:
    print(inter.data, end=' -> ')
    inter = inter.next
print("None")
