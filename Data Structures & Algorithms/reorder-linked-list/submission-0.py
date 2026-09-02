# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        half = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        slow.next = None

        #reverse order of second half
        half = self.reverse(half)
        curr = head
        
        while half:
            nxt1 = curr.next
            nxt2 = half.next

            curr.next = half
            half.next = nxt1

            curr = nxt1
            half = nxt2           

        