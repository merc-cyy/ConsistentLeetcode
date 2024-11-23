#Given a binary array nums, return the maximum number of consecutive 1's in the array.


#Input: array of int 1 or 0
#OUtput: maximum number of consecutive ones
#Task: count the max number of consecutive ones and return it
#Ideas:
#1. Iterate through list counting ones and at zero restart count. return max.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #iterate through the list
        #check if 1/0
        #if 1: increment count
        #2. if 0: max(maxCount, count) then restrart count.
        maxCount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                maxCount = max(maxCount, count)
            elif i == 0:
                maxCount = max(maxCount, count)
                count = 0
        return maxCount
#CQs: is inout always as indicated? error for any wrong args or?
#edge cases: all 0s, all 1s, wrong args, 
#Time: O(n)
#Space:0(1)
        