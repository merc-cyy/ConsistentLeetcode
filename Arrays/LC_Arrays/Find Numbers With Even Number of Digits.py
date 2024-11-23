#Given an array nums of integers, return how many of them contain an even number of digits.

#My idea
#input: array of int
#output: int, number of ints in array that contain even number of digits
#task: count number of digits in each, check if even
#ideas: 1. for each int, convert to str and get len
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #loop through list
        #convert to str and get length, check if even
        #if even update count
        #return count
        count = 0
        for i in nums:
            digits_length = len(str(i))
            if (digits_length % 2 == 0):#even
                count += 1
        return count

#Other answer
#You can get number of digits by: 
# 1. dividing by ten
# function hasEvenDigits(num)
# {    
#     digitCount = 0
#     while num is not 0
#     {
#         digit = num % 10 ##to get remainder
#         digitCount = digitCount + 1
#         num = num / 10
#     }

#     if digitCount % 2 == 0
#         return true
#     else
#         return false
# }#Time is now O(n log m)where m is the max int in the array. Log m because you can only divide a number m by a value y log to base y times.(in this case, y = 10)

#2. log method
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         # Counter to count the number of even digit integers
#         even_digit_count = 0

#         for num in nums:
#             # Compute the number of digits in num
#             digit_count = int(math.floor(math.log10(num))) + 1
#             if digit_count % 2 == 0:
#                 even_digit_count += 1

#         return even_digit_count
# }#Time is now O(n log m)where m is the max int in the array. Log m because you can only divide a number m by a value y log to base y times.(in this case, y = 10)


        