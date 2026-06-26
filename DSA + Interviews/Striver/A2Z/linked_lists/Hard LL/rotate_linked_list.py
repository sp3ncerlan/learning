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

"""
First grab the kth node
Then we set a pointer to the beginning of the next section which we will use as the next of the end for the current section
We reverse all the section until k

Then we need to save the first of the current section (which would be groupEnd.next) so that we can refer to it as the end of the current section
    - groupEnd.next = the new head of the reversed section
    - move groupEnd to the holder to set up for the next section
"""

def func(head, k):
    if not head or not head.next or k == 0:
        return head
    
    length = 1
    
    # find length
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
        
    tail.next = head
    
    k = k % length
    num_of_steps_to_new_tail = length - k
    
    new_tail = head
    for _ in range(num_of_steps_to_new_tail - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

arr = [1, 2, 3, 4, 5]
k = 2
new_list = LinkedList(arr)
new_list.print_list()
new_list.head = func(new_list.head, k)
print(new_list.print_list())

"""
Problem Statement: Given the head of a singly linked list containing integers, shift the elements of the linked list to the right by k places and return the head of the modified list. Do not change the values of the nodes, only change the links between nodes.

Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output : head -> 4 -> 5 -> 1 -> 2 -> 3
Explanation :List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.

Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 4
Output :head -> 2 -> 3 -> 4 -> 5 -> 1
Explanation :List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.
List after 3 shift to right: head -> 3 -> 4 -> 5 -> 1 -> 2.
List after 4 shift to right: head -> 2 -> 3 -> 4 -> 5 -> 1. 
"""
