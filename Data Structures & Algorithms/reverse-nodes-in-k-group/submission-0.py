# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         nodes_reversed = 1
#         prev_tail = None
#         prev = head
#         current = head.next
#         while current:
#             nextPtr = current.next
#             current.next = prev
#             prev = current
#             current = nextPtr
#             nodes_reversed += 1
#             if nodes_reversed == k:
#                 next_head = prev
#                 if prev_tail:
#                     prev_tail.next = next_head
#                 prev_tail = current
#                 nodes_reversed = 1
#                 if current:
#                     current = current.next
#         return head
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find kth node
        def getkth(curr, k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr
        dummy = ListNode(0, head)
        prev_tail = dummy
        
        while True:
            kth = getkth(prev_tail, k)
            if not kth:
                break
            next_tail = kth.next
            prev = kth.next
            current = prev_tail.next
            # reverse group
            while current != next_tail:
                nextPtr = current.next
                current.next = prev
                prev = current
                current = nextPtr

            tmp = prev_tail.next
            prev_tail.next = kth
            prev_tail = tmp
        return dummy.next



