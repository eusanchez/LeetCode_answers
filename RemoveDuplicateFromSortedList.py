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

        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                # remove the duplicate
                current_node.next = current_node.next.next
            else:
                # move forward only if no removal
                current_node = current_node.next
        return head
