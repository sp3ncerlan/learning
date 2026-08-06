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
    # function to reverse the linked list
    def reverseList(self, node):
        prev = None
        curr = node
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev

    # Function to add one to the number represented by the linked list
    def addOne(self, head):
        # 9 -> 2 -> 1
        
        head = self.reverseList(head)
        curr = head
        carry = 1
        
        while curr and carry:
            total = curr.data + carry
            carry = total // 10
            
            curr.data = (total % 10)
            
            if not curr.next and carry:
                curr.next = Node(carry)
                carry = 0
                break
            
            curr = curr.next
            
        return self.reverseList(head)

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
