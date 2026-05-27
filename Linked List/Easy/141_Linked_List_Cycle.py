# Linked List Cycle Detection using Floyd’s Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        Detects if a linked list has a cycle.

        :type head: ListNode
        :rtype: bool
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
