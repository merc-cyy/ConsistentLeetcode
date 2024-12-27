class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)#length of s
        ans = 0#ans variable
        # charToNextIndex stores the index after current character
        charToNextIndex = {}#a set that stores the characters and the index of the character that occurs AFTER that occurence

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:#if the key already exists
                i = max(charToNextIndex[s[j]], i)#to move the left pointer from where it was to the index AFTER the occurence(removing duplicates)

            ans = max(ans, j - i + 1)#calculate the length of that substring and get max against what had been initially saved
            charToNextIndex[s[j]] = j + 1#adding values to the set

        return ans
    
"""
so basically how this sliding window works is that for each ch, it adds it to a set where the value is the index after it(to jump duplicates)
if the ch is not in the dict:
add it and the index after, check length of substring 

"""