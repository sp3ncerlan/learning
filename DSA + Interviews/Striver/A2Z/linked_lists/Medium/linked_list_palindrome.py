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
    if not head or not head.next:
        return True
    
    slow, fast = head, head
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    if fast:
        slow = slow.next
        
    # split list
    prev.next = None
        
    # reverse
    second_head = reverse(slow)
    
    first, second = head, second_head
    is_palindrome = True
    
    while second:
        if first.val != second.val:
            is_palindrome = False
            break
        
        first = first.next
        second = second.next
        
    # rearrange back
    restored = reverse(second_head)
    prev.next = restored
    
    return is_palindrome

def reverse(head):
    prev = None
    curr = head
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    # prev sits at the second_head
    return prev

arr = [3, 7, 5, 7, 3]
new_list = LinkedList(arr)
new_list.print_list()
print(func(new_list.head))
"""
Problem Statement: Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false. .

A palindrome is a sequence that reads the same forward and backwards.

Example 1:
Input: head -> 3 -> 7 -> 5 -> 7 -> 3
Output: true
Explanation: 37573 is a palindrome.

Example 2:
Input: head -> 1 -> 1 -> 2 -> 1
Output: false
Explanation: 1121 is not a palindrome.
"""
