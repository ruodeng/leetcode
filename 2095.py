# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    x=0
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        levels = 1
        def dfs(head,levels):
            if not head.next:
                self.x = levels//2
                print("self.x", self.x)
                return head

            if self.x == levels:
                print('remove this')
                head.next = head.next.next
            else:
                head.next = dfs(head.next, levels + 1)
            return head
        return dfs(head,levels)


s = Solution()
print(s.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

