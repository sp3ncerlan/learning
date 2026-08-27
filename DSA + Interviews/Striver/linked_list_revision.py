import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to merge k sorted linked lists using a min-heap
    def mergeKLists(self, lists):
        min_heap = []

        temp = curr = ListNode(-1)

        # prepopulate
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))

        while min_heap:
            _, index, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return temp.next

# Driver code
if __name__ == "__main__":
    sol = Solution()

    # Creating three linked lists:
    # list1: 1 -> 4 -> 5
    # list2: 1 -> 3 -> 4
    # list3: 2 -> 6

    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    result = sol.mergeKLists(lists)

    # Print the merged list
    while result:
        print(result.val, end=" ")
        result = result.next
