class Node:
    def __init__(self, val):
        self.num = val
        self.next = None
        
    # Utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

def intersection(l1, l2):
    temp1, temp2 = l1, l2
    
    while temp1 != temp2:
        temp1 = l2 if temp1 is None else temp1.next
        temp2 = l1 if temp2 is None else temp2.next
    
    return temp1

# Utility function to print linked list
def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

# Driver code
head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing the lists
print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

# Checking if intersection is present
answerNode = intersection(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")

"""
Problem Statement: Given a linked list containing only 0's, 1's, and 2's, sort the linked list by rearranging the links (not by changing the data values).

Input: 1 -> 2 -> 0 -> 1 -> 0 -> 2 -> NULL
Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> NULL
Input: 2 -> 1 -> 2 -> 0 -> 0 -> 1 -> NULL
Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> NULL

OPTIMAL:
- three chains of 0 1 and 2, then combine at the end
"""
