# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # data = {}
        # count = 0
        # while head:
        #     if head in data:
        #         return True
        #     data[head] = count
        #     head = head.next
        # return False


        # Usin Floyd cycle finding algorithm
        slow = fast = head
        while fast and fast.next :
            slow = slow.next
            fast =fast.next.next
            if slow == fast:
                return True
        return False

        