-- INCOMPLETE -- 

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = head
        elemento_actual = head.val
        elemento_vecino = head.next.val

        while current_node:
            if elemento_actual == elemento_vecino:
                head = head.next
            current_node = current_node.next


