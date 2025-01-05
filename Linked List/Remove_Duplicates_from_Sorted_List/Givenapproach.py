# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #input: head of a sorted list
        #output: head of list 
        #goal: remove all duplicates in the list
        #task: find the duplicates, how to remove them
        #approach 1: check if curr is equal to curr.next  skip the curr.next so we don't have to remove the head if the first val is duplicated. check again if curr is equal to curr.next in case we have more duplicates. if not, shift curr to the next val

        curr = head#start it off at the head

        while curr: #till you drop out of the list
            while curr.next and curr.val == curr.next.val:
                #while more duplicates exist and we check for curr.next to avoid trying to access curr.next if curr is at the end
                curr.next = curr.next.next#skip the duplicate ahead
            curr = curr.next#increment curr

        return head



        