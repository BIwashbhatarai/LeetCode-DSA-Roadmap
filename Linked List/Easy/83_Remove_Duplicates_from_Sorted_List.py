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

        current = head

        if current is None:
            return head

        while current and current.next:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next

        return head
