#Fast and Slow Approach
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        double=single=head
        while double and double.next:
            single=single.next
            double=double.next.next
        return single
        