class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: a sorted array, target
        #output: index of target else -1
        #goal: binary search
        #task: do binary search

        #approach: go to the midway, if smaller, check the right side, if larger, check the left side

        l = 0
        r = len(nums) - 1

        while l <= r:#equal to because if they are equal to we haven't checked the number yet
            m = (l + r) // 2#int division
            val = nums[m]
            if val < target:#check the right side
                l = m + 1
            elif val > target:
                r = m -1
            else:#equal
                return m

        return -1#not found
        