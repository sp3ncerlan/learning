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

def func(head):
    even, odd = ListNode(0), ListNode(0)
    even_temp, odd_temp = even, odd
    
    curr = head
    while curr:
        if curr.val % 2 == 0:
            even.next = curr
            even = even.next
        else:
            odd.next = curr
            odd = odd.next
        curr = curr.next

    # point even tail to odd head
    even.next = odd_temp.next
    odd.next = None
    
    return even_temp.next

arr = [1, 2, 3, 4, 5, 6]
new_list = LinkedList(arr)
new_list.print_list()
new_head = func(new_list.head)
result_list = LinkedList()
result_list.head = new_head
result_list.print_list()

"""
Problem Statement: Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list. Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.

Input: 1→2→3→4→5→6→Null
Output: 2→4→6→1→3→5→Null
Explanation : Odd Nodes in LinkedList are 1,3,5 and Even Nodes in LinkedList are 2,4,6
In Modified LinkedList all even Nodes comes before all Odd Nodes. So Modified LinkedList looks like 2→4→6→1→3→5→Null. Order of even and odd Nodes is 
maintained in modified LinkedList.

Input: 1→3→5→Null
Output: 1→3→5→Null
Explanation: As there are no Even Nodes in LinkedList, The Modified LinkedList is same as Original LinkedList.
"""
