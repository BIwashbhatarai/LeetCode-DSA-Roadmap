# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow, fast = head, head

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # If fast is None, remove the head
        if fast is None:
            return head.next

        # Move both pointers until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return head
