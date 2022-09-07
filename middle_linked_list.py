# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while True:
            slow = slow.next

            if not fast.next or not fast.next.next:
                return slow

            fast = fast.next.next
