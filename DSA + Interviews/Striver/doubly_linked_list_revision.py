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

def deleteAllOccurrences(head, target):
    curr = head
    while curr:
        if curr.val == target:
            next_node = curr.next
            if curr == head:
                head = head.next
                if head:
                    head.prev = None
            else:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            
        curr = curr.next
            
    return head

# --- Test Cases ---

# Test Case 1: Example from description
head1 = create_dll([1, 2, 3, 1, 4])
res1 = deleteAllOccurrences(head1, 1)
print("Test 1:", dll_to_list(res1))  # Expected: [2, 3, 4]

# Test Case 2: Removing all elements
head2 = create_dll([7, 7, 7, 7])
res2 = deleteAllOccurrences(head2, 7)
print("Test 2:", dll_to_list(res2))  # Expected: []

# Test Case 3: Target not present
head3 = create_dll([1, 2, 3])
res3 = deleteAllOccurrences(head3, 5)
print("Test 3:", dll_to_list(res3))  # Expected: [1, 2, 3]

# Test Case 4: Empty list
head4 = create_dll([])
res4 = deleteAllOccurrences(head4, 1)
print("Test 4:", dll_to_list(res4))  # Expected: []
