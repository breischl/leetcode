from typing import Optional
from collections import deque

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Using the naive approach of just shoving the whole thing into a double-ended queue, then pairwise comparing the elements from each end of that queue
        # This could probably be sped up a bit by not actually popping elements, just comparing them. But I don't care that much.
        #
        # The fancy approach involves a lot of pointer manipulation to find the midpoint of the list (using a fast/slow pointer algorithm) then reversing half of the list and walking it again

        queue: deque[int] = deque()
        while head:
            queue.append(head.val)
            head = head.next

        while len(queue) > 1:
            if queue.pop() != queue.popleft():
                return False

        return True
