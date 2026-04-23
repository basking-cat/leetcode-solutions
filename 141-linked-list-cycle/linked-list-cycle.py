# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       # we use two pointers
       # one is slow(visits every node), one is fast(visits every other node)
       # slow starts from the first element, and fast starts from the 2nd element
       # if a list has a cycle in it, the two pointers will eventually meet somewhere

       if not head:
         return False

       slow, fast = head, head

       while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

       return False