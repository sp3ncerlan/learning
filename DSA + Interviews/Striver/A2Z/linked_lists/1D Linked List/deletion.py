class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def build_list(arr):
    temp = ListNode(0)
    curr = temp
    
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    
    return temp.next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    
    print("None")

def func(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node
    
arr = [0, 1, 2]
val = 5
list1 = build_list(arr)
result = func(list1, val)
print_list(result)
