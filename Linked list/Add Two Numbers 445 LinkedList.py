# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        total = num1 + num2

        print(total)
        curr = head = ListNode(0)
        if total == 0:
            return head

        while total != 0:
            head.next = ListNode(total % 10)
            total = total // 10
            head = head.next
        prev = None
        head = curr.next
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
