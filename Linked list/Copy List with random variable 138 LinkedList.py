"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        curr = head
        # Step 1 insering new nodes in between
        while curr:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = temp
        curr = head
        # 2 Setting random pointers
        while curr:
            if curr.next:
                curr.next.random = None if curr.random is None else curr.random.next

            curr = curr.next.next
        # 3 Separating the original with copy
        original = head
        copy = head.next
        temp = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        return temp


