# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left_pointer = dummy_node
        right_pointer = head
        while n > 0 and right_pointer:
            right_pointer = right_pointer.next
            n -= 1
        
        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
            
        left_pointer.next = left_pointer.next.next
        return (dummy_node.next)