# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0)
        end = result
        carry = 0
        
        while l1 or l2 or carry:
            r1 = (l1.val if l1 else 0)
            r2 = (l2.val if l2 else 0)
            carry, temp_sum = divmod(r1+r2+carry, 10)
            
            end.next = ListNode(temp_sum)
            end = end.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return result.next
        
