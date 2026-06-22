# Node class represents a node in a linked list
class Node:
    # Constructor with data and optional next node
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node in the list
        self.next = next1

# Solution class containing the delete function
class Solution:
    def merge(self, l1, l2):
        temp = Node(0)
        curr = temp
        
        while l1 and l2:
            if l1.data <= l2.data:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return temp.next
        
    def findMiddle(self, head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def sort(self, head):
        if not head or not head.next:
            return head
            
        middle = self.findMiddle(head)
        
        right = middle.next
        middle.next = None
        left = head
        
        left = self.sort(left)
        right = self.sort(right)
        
        return self.merge(left, right)

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
    head = Node(3)
    head.next = Node(4)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(5)

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
Problem Statement: Given a linked list, sort its nodes based on the data value in them. Return the head of the sorted linked list.

Input: 3->4->2->1->5 
Output: 1->2->3->4->5


BF:
- just create a new linked list, go through the original and find the next number while keeping a count and stringing it to the new linked list

OPTIMAL:
- just replace the number after grabbing count
- o(n * 2)
- o(1) space
"""
