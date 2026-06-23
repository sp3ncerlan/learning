# Node class representing a single digit in the linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# LinkedList class to manage node-level operations
class LinkedList:
    # function to insert digit at the end
    def append(self, head, value):
        new_node = Node(value)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

    # Function to print the list
    def printList(self, head):
        current = head
        while current:
            print(current.data, end='')
            current = current.next
        print()
        
# Solution class having the addOne logic 
class Solution:
    def palindrome(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_head = self.reverse(slow)
        first, second = head, second_head
        
        
        
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev    
        
# Main function
if __name__ == "__main__":
    head = None
    ll = LinkedList()
    sol = Solution()

    # Example: Number 129 (1 -> 2 -> 9)
    head = ll.append(head, 1)
    head = ll.append(head, 2)
    head = ll.append(head, 9)

    print("Original Number: ", end='')
    ll.printList(head)

    head = sol.addOne(head)

    print("After Adding One: ", end='')
    ll.printList(head)
