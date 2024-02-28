# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = 0
        p = head
        while p:
            i += 1
            if i % k == 0:
                pre = self.reverse(pre, p.next)
                p = pre.next
            else:
                p = p.next
        return dummy.next
    def reverse(self, pre, next):
        last = pre.next
        cur = last.next
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last