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

        pointer1, pointer2 = headA, headB

        while pointer1 != pointer2:
            pointer1 = pointer1.next if pointer1 else headB
            pointer2 = pointer2.next if pointer2 else headA
        return pointer1 