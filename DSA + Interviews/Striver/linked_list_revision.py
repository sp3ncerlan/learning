class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    ''' Merge the two linked lists in a particular
     order based on the data value '''
    def merge(self, list1, list2):
        temp = current = ListNode(-1)
        
        while list1 and list2:
            if list1.val < list2.val:
                current.child = list1
                list1 = list1.child
            else:
                current.child = list2
                list2 = list2.child
                
            current = current.child
            
        if list1:
            current.child = list1
        else:
            current.child = list2
            
        return temp.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        if not head or not head.next:
            return head
        
        next_head = self.flattenLinkedList(head.next)
        
        # merge
        merged = self.merge(head, next_head)
        
        head.next = None
        
        return merged

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
# Corrected properly sorted driver code
    head = ListNode(5)
    head.child = ListNode(7)
    head.child.child = ListNode(8)
    head.child.child.child = ListNode(30)

    head.next = ListNode(10)
    head.next.child = ListNode(20)

    head.next.next = ListNode(19)
    head.next.next.child = ListNode(22)
    head.next.next.child.child = ListNode(50)

    head.next.next.next = ListNode(28)
    head.next.next.next.child = ListNode(35)
    head.next.next.next.child.child = ListNode(40)
    head.next.next.next.child.child.child = ListNode(45)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)
