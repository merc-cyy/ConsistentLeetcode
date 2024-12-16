"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

#Understand
#input: an array of size int in increasing order with some duplicates
#output: number of unique elements
#goal: remove all duplicate elements in-place; array remains same size; first k values of array are the unique elements then the other values can be anything;
#[0,0,1,1,1,2,2,3,3,4]= [0,1,2,3,4,_,_,_,_,_]

#Approach 1: Using Auxiliary space(a queue and a set)
"""
vals=set()
k = 0
for i in arr:
    if i not in set:
        put i in set
        put into the queue
        k +=1

for i in range(0,k+1):
    dequeue and modify array


"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        vals = {}
        k = 0
        queue = []
        for i in nums:
            if i not in vals:
                vals[i] = ""
                queue.append(i)
                k += 1
        print(f"queue_len:{len(queue)}")
        print(f"k:{k}")

        for idx in range(0, k):
            nums[idx] = queue.pop(0)
        return k
    

#Approach 2:no auxiliary space
