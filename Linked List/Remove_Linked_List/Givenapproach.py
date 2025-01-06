# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #input: head of a list
        #output: head
        #goal: remove all occurrences of val
        #task: find val, remove it/skip it
        #approach: have a prev ptr if curr is val, skip it, only advance prev if we have't skipped a value
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        #loop while head.next
        while curr:
        #check if curr is 6, skip it
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next#only advance prev if there was no skip
        #advance
            curr = curr.next
        #return head
        return dummy.next


        