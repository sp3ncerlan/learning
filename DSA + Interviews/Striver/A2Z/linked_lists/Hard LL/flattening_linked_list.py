class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def recurse(head1, head2):
    temp = ListNode(0)
    res = temp
    
    while head1 and head2:
        if head1.val < head2.val:
            res.child = head1
            res = res.child
            head1 = head1.child
        else:
            res.child = head2
            res = res.child
            head2 = head2.child
            
        res.next = None
        
    if head1:
        res.child = head1
    else:
        res.child = head2
        
    if temp.child:
        temp.child.next = None
        
    return temp.child

def flattenLinkedList(head):
    if not head or not head.next:
        return head
    
    merged_head = flattenLinkedList(head.next)
    
    head = recurse(head, merged_head)
    
    return head

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        ''' If child exists, recursively
         print it with indentation '''
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next
        
if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)
    
    # Function call to flatten the linked list
    flattened = flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)

"""
Problem Statement: Given a linked list containing 'N' head nodes where every node in the linked list contains two pointers:

'Next' points to the next node in the list
'Child' pointer to a linked list where the current node is the head

Each of these child linked lists is in sorted order and connected by a 'child' pointer. Your task is to flatten this linked list such that all nodes appear in a single layer or level in a 'sorted order'.

Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output :head -> 2 -> 1 -> 4 -> 3 -> 5
Explanation :The groups 1 -> 2 and 3 -> 4 were reversed as 2 -> 1 and 4 -> 3.

Input :head -> 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output :head -> 3 -> 2 -> 1 -> 4 -> 5
Explanation :The groups 1 -> 2 -> 3 were reversed as 3 -> 2 -> 1.
Note that 4 -> 5 was not reversed.
"""
