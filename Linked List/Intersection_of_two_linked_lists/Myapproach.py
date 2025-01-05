# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #input: two heads
        #output: node of intersection or null
        #goal: check if two linked lists intersect
        #task: is there any node that both lists share?
        #constraints: no cycles; we can have duplicates(so we need to check if the nodes themselves are equal), dont modify the linked list structure
        #approach1: add all nodes in list1 into a hash set, iterate again through list2 and check if any are in the hash set. (nodes not vals)
        #approach2: iterate thrhough both to get their lenghts, start off both ptrs at the same length and go comparing. if same, return true
        #approach3: move both ptrs and if one list runs out, wrap to the next list and do the same for the other and go checking if nodes are equal

        ptr1, ptr2 = headA, headB
        len1 = 0
        len2 = 0
        #get length of both linked lists
        while ptr1:
            len1 += 1
            ptr1 = ptr1.next
        #print(len1)

        while ptr2:
            len2 += 1
            ptr2 = ptr2.next
        #print(len2)

        ptr1, ptr2 = headA, headB #restart them off at the start
        #print(ptr)
        #get starting point
        if len2 >= len1:
            diff = len2 - len1 
            for i in range(diff):
                ptr2 = ptr2.next#get it to the same starting point
        else:
            diff = len1 - len2
            for i in range(diff):
                ptr1 = ptr1.next

        while ptr1 and ptr2:#not none
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return None

        


        