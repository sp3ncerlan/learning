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
    temp = groupEnd = ListNode(0, head)
    
    while True:
        kth = getKthNode(groupEnd, k)
        if not kth:
            break
        
        prev = kth.next
        curr = groupEnd.next
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        holder = groupEnd.next # holder = 3
        groupEnd.next = kth # groupEnd.next = 4
        groupEnd = holder # move groupEnd to end of the current section to set up for next section
        
    return temp.next
    
def getKthNode(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    
    return curr

arr = [1, 2, 3, 4, 5]
k = 2
new_list = LinkedList(arr)
new_list.print_list()
new_list.head = func(new_list.head, k)
print(new_list.print_list())

"""
Problem Statement: Given the head of a singly linked list containing integers, reverse the nodes of the list in groups of k and return the head of the modified list. If the number of nodes is not a multiple of k, then the remaining nodes at the end should be kept as is and not reversed.
Do not change the values of the nodes, only change the links between nodes.

Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output :head -> 2 -> 1 -> 4 -> 3 -> 5
Explanation :The groups 1 -> 2 and 3 -> 4 were reversed as 2 -> 1 and 4 -> 3.

Input :head -> 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output :head -> 3 -> 2 -> 1 -> 4 -> 5
Explanation :The groups 1 -> 2 -> 3 were reversed as 3 -> 2 -> 1.
Note that 4 -> 5 was not reversed.
"""
