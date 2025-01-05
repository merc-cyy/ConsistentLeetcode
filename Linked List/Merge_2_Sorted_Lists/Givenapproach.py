# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #input: head of a list
        #output: t or f
        #goal: check if there is a cycle
        #task: can you go and reach a node we had already visited? how can you tell if its a node we already visited?
        #approach 1; use a hash set and append the node itself(val.next); check if a node is in the set already. append the node itself not the value since we could have duplicates
        #approach 2; optimal space
        #

        