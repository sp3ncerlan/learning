# Node class to represent
# elements in the linked list
class Node:
    # Data stored in the node
    def __init__(self, x):
        self.data = x
        # Pointer to the next node
        self.next = None
        # Pointer to a random
        # node in the list
        self.random = None

# Function to insert a copy of each
# node in between the original nodes
def insertCopyInBetween(head):
    curr = head
    while curr and curr.next:
        next = curr.next
        
        copy = Node(curr.data)
        
        curr.next = copy
        copy.next = next
        
        curr = next

# Function to connect random
# pointers of the copied nodes
def connectRandomPointers(head):
    real = head
    
    while real:
        clone = real.next
        clone.next = real.next.next
    
# Function to retrieve the
# deep copy of the linked list
def getDeepCopyList(head):
    temp = head
    
    dummy = Node(-1)
    
    res = dummy
    while temp:
        res.next = temp.next
        res = res.next
        
        temp.next = temp.next.next
        temp = temp.next
        
    return dummy.next

# Function to clone the linked list
def cloneLL(head):
    

# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head:
        print("Data:", head.data, end="")
        if head.random:
            print(", Random:", head.random.data, end="")
        else:
            print(", Random: None", end="")
        print()
        # Move to the next node
        head = head.next

# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    clonedList = cloneLL(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)

"""
Problem Statement: Given a linked list where every node in the linked list contains two pointers:

'next' which points to the next node in the list.
'random' which points to a random node in the list or 'null'.
Create a 'deep copy' of the given linked list and return it.

Example 1:                
Input: [[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]]
Output: 1 2 3 4 5, true
Explanation: All the nodes in the new list have same corresponding values as original nodes.
All the random pointers point to their corresponding nodes in the new list.
'true' represents that the nodes and references were created new.

Example 2: 
Input: [[5, -1], [3, -1], [2, 1], [1, 1]]
Output: 5 3 2 1, true
Explanation: All the nodes in the new list have same corresponding values as original nodes.
All the random pointers point to their corresponding nodes in the new list.
'true' represents that the nodes and references were created new.
[[5, -1], [3, -1], [2, -1], [1, -1]] will be incorrect, although it has the same values.
"""
