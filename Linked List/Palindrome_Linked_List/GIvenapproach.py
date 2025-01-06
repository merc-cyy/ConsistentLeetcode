# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #inout: head
        #output: t or f
        #goal: is it a palindrome?
        #task: is it the same frontwards and backwards?
        #approach1:  go to the middle and reverse the rest of the list and compare if equal
        #approach2: convert to array and check if palindrome

        if not head.next:
            return True#one node
        #go to the middle and slice
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        temp_half = slow.next
        slow.next = None
        second = temp_half
        
        #reverse the rest
        prev = None
        while second:
            temp_r = second.next
            second.next = prev#reverses
            prev = second
            second = temp_r

        #compare
        while first and prev:
            if first.val != prev.val:
                return False
            first = first.next
            prev = prev.next
        
        return True
        