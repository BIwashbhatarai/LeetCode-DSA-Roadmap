# LeetCode 92. Reverse Linked List II
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        # Edge case: empty list or no reversal needed
        if not head or left == right:
            return head

        prev = None
        current = head

        # Move to the starting position of reversal
        for _ in range(left - 1):
            prev = current
            current = current.next

        # Store connections
        connection = prev
        tail = current

        # Reverse the sublist
        prev = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Reconnect the reversed sublist
        if connection:
            connection.next = prev
        else:
            head = prev

        tail.next = current

        return head
