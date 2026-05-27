# Middle of the Linked List using Two Pointers (Fast & Slow)
# Time Complexity: O(n)
# Space Complexity: O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        Returns the middle node of the linked list.

        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
