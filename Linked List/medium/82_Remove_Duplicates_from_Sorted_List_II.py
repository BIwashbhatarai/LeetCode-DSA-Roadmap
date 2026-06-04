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

        # Fix duplicates at the beginning of the list
        while head and head.next:
            if head.val != head.next.val:
                break

            dup_val = head.val

            while head and head.val == dup_val:
                head = head.next

        if not head:
            return None

        prev = head
        curr = head.next

        while curr:
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val

                while curr and curr.val == dup_val:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return head
