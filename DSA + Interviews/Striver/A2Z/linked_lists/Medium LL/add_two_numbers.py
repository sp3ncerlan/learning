# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        # Value stored in the node
        self.val = val    
        # Pointer to the next node
        self.next = next  

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = curr = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            
            total = l1_value + l2_value + carry
            value = total % 10
            carry = total // 10
            
            curr.next = ListNode(value)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next
        
def create_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    num1 = [2, 4, 3]  # represents 342
    num2 = [5, 6, 4]  # represents 465
    l1 = create_list(num1)
    l2 = create_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # Output: 7 -> 0 -> 8
