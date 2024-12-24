class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: array of int
        #output: array of int
        #goal: return an array where each val is the product of everything in the array except itself
        #steps: create two arrays: prefix and suffix then create a new array combining the relevant indices

        result = [1 for i in range(len(nums))]#initirrayliaze the result a

        prefix = 1
        suffix = 1
        for i in range(len(nums)):#iterate through the array from left to right
            result[i] = prefix#the array frist stores the prefixes
            prefix *= nums[i] #update prefix to hold the current val
            #this updates the array to hold the prefixes

        for i in range(len(nums), -1, -1):#iterate through array from right to left
            result[i] *= suffix 
            suffix *= nums[i]

        return result





