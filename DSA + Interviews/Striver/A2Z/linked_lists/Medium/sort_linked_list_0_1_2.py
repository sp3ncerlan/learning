# Node class represents a node in a linked list
class Node:
    # Constructor with data and optional next node
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node in the list
        self.next = next1

class Solution:
    def sort(self, head):
        zero, one, two = Node(0), Node(0), Node(0)
        zero_start, one_start, two_start = zero, one, two
        
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
        
        zero.next = one_start.next
        one.next = two_start.next
        two.next = None
        
        return zero_start.next

# Function to print the linked list
def printLL(head):
    # Initialize a temporary pointer
    temp = head
    # Traverse the linked list and print data
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    # Print a newline after the list
    print()

# Driver code
if __name__ == "__main__":
    # Creating a sample linked list
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)
    head.next.next.next.next.next = Node(2)

    # Display the original linked list
    print("Original Linked List:", end=" ")
    printLL(head)

    # Create a Solution object
    obj = Solution()
    # Deleting the middle node
    head = obj.sort(head)

    # Displaying the updated linked list
    print("Updated Linked List:", end=" ")
    printLL(head)

"""
Problem Statement: Given a linked list containing only 0's, 1's, and 2's, sort the linked list by rearranging the links (not by changing the data values).

Input: 1 -> 2 -> 0 -> 1 -> 0 -> 2 -> NULL
Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> NULL
Input: 2 -> 1 -> 2 -> 0 -> 0 -> 1 -> NULL
Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> NULL

OPTIMAL:
- three chains of 0 1 and 2, then combine at the end
"""
