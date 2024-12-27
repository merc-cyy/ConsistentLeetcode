class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: a string
        #output: int(length of the longest substring without any repeating characters)
        #goal: find the longest substring without repeating characters
        #steps: two pointers at the start
        # increment r while not in set, 
        #if in set, move l to the index in front of the repeated character
        #compare the length of the substring now and update that to be the max

        l = r = 0
        length = r - l
        characters = {}

        while r < len(s):
            if s[r] not in characters:
                characters[s[r]] = r#add to the set
                current_l = r - l + 1
                length = max(length, current_l)
                r += 1
            else:
                #repeat_index = characters.get(s[r])
                print(s[l])
                characters.pop(s[l])
                l += 1

        return length


        