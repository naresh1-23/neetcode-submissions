# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        sum = 0 
        while l1 and l2:
            sum = l1.val + l2.val + sum
            digit = sum %10
            result.next = ListNode(digit)
            sum //=10
            result =result.next
            l1 =l1.next
            l2 = l2.next
        if l1:
            while l1:
                sum+=l1.val
                digit = sum %10
                result.next = ListNode(digit)
                sum //=10
                result =result.next
                l1 = l1.next

        if l2:
            while l2:
                sum+=l2.val
                digit = sum %10
                result.next = ListNode(digit)
                sum //=10
                result =result.next
                l2=l2.next
        while sum > 0:
            digit = sum%10
            result.next = ListNode(digit)
            sum//=10
            result = result.next
                    
        return dummy.next
        

        