class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, arr=None):
        self.head = None
        
        if arr:
            self.head = self.build(arr)

    # ------------------------
    # BUILD / CONVERT
    # ------------------------
    def build(self, arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def to_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    # ------------------------
    # PRINT
    # ------------------------
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

def func(head, N):
    temp = ListNode(0, head)
    
    p2 = temp
    for _ in range(N):
        p2 = p2.next
    
    p1 = temp
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    
    p1.next = p1.next.next
    
    return temp.next
        
arr = [1, 2, 3, 4, 5]
N = 3
problem_list = LinkedList(arr)
result_head = func(problem_list.head, N)
result_list = LinkedList()
result_list.head = result_head
result_list.print_list()

"""
Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.

Input:  5->1->2, N=2
Output: 5->2
Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.

Input:  1->2->3->4->5, N=3
Output: 1->2->4->5
Explanation: The 3rd node from the end is 3, therefore, we remove 3 from the linked list.
"""
