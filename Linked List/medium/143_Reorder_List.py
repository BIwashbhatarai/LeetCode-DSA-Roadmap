# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None
        Do not return anything, modify head in-place instead.
        """

        # Find middle of the linked list
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_half = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        current = second_half

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Merge two halves
        first = first_half
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
