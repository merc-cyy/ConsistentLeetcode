class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #input:array of nums
        #output: t or f is all elements are distinct
        #goal: find if an array has duplicates
        #steps: make a dict, iterate through array, checking if element exists

        values = {}
        for i in nums:
            if i not in values:
                values[i] = ""
            else:
                return True

        return False
        