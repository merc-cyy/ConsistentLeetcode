"""
Approach 1
Use two pointers. Start both at index 1 since we know the val at index 0 is always unique and doesn't need to be moved
if current is not same as previous:(we know all duplicates will be in consecutive order)
one pointer is keeping track of where the unique elements should go so update array as you move

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        unique_index = 1

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index