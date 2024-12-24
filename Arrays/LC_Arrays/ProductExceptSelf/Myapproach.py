class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: array of int
        #output: array of int
        #goal: return an array where each val is the product of everything in the array except itself
        #steps: create two arrays: prefix and suffix then create a new array combining the relevant indices

        #create two arrays prefix and suffix
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] * prefix[i-1])
        print(prefix)
        
        suffix = [1 for i in range(len(nums))]
        suffix[len(nums)-1] = nums[len(nums)-1]#place the last value
        for j in range(len(nums)-2, -1, -1):#iterate from the back
            suffix[j] = suffix[j+1] * nums[j]
        print(suffix)
        #create a new array and populate it using appropriate values from prefix and suffix
        ans = [1 for i in range(len(nums))]
    
        for idx in range(len(nums)):
            #to handle edge values
            if idx == 0:
                ans[idx] = suffix[idx+1]
            elif idx == len(ans) - 1:
                ans[idx] = prefix[idx-1]
            else:
                ans[idx] = prefix[idx-1] * suffix[idx+1]

        return ans
    
    #space = o(n)
    #time= o(n)
"""
The next challenge is to do it in o(1) space


"""
        