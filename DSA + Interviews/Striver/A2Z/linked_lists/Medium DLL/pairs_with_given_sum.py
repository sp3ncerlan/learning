# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
# Helper function to build a DLL from a Python list
def create_dll(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        new_node = ListNode(val)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    return head

# Helper function to convert DLL back to Python list to verify structure
def dll_to_list(head):
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        # Optional: Verify integrity of forward/backward links
        if curr.next and curr.next.prev != curr:
            print(f"Warning: Broken link at node {curr.val}")
        curr = curr.next
    return lst

def pairs_given_sum(head, target):
    result = []
    
    if not head:
        return result
    
    left = head
    
    # find tail
    right = head
    while right.next:
        right = right.next
        
    while left != right and right.next != left:
        total = left.val + right.val
        
        if total == target:
            result.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif total < target:
            left = left.next
        else:
            right = right.prev
            
    return result

# --- Test Cases ---

# Test Case 1: Example from description
head1 = create_dll([1, 2, 4, 5, 6, 8, 9])
res1 = pairs_given_sum(head1, 7)
print("Test 1:", res1)  # Expected: [2, 3, 4]
