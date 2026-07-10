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

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        next_distinct = curr.next
        
        while next_distinct and next_distinct.val == curr.val:
            next_distinct = next_distinct.next
        
        curr.next = next_distinct
        if next_distinct:
            next_distinct.prev = curr
        
        curr = curr.next
        
    return head

# --- Test Cases ---

# Test Case 1: Example from description
head1 = create_dll([1, 1, 3, 3, 4, 5])
res1 = remove_duplicates(head1)
print("Test 1:", dll_to_list(res1))  # Expected: [2, 3, 4]
