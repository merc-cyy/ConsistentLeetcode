"""
Approach 1: Bucket sort

so we want the k top frequent elements. We can use bucket sort in that we have an array same len as len of input nums
So the index represents the freq of occurrence then the value at that index is a list of values that occur that many times.
Once we have that,  we want to return the top k items so that means we iterate through the array from the end.

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input: array of int and int k
        #output: array of int
        #goal: return top k most freq elements

        #steps: first create a dict with values and their count
        #       create the bucketsort array where the count is the index and the value at that index is a list of values with that same count
        #       then iterate through the array returning the items from the back

        count_dict = {}#created a dict holding the values and their counts
        for i in nums:#update
            if i in count_dict:
                count_dict[i] += 1# coutn_dict[i] = count_dict.get(i,0) --places a default val of 0
            else:#add a new val
                count_dict[i] = 1

        #freq = [[]] * (len(nums) + 1)#an array storing the counts as indexes
        # This line creates a list of lists where all sublists reference the same memory location. This means any change to one sublist will affect all sublists.
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count_dict.items():#populate the array
            freq[count].append(num)

        res=[]
        for j in range(len(nums), 0, -1):#iterate through freq array backwards 
            for v in freq[j]:#iterate through the list at each slot in freq
                res.append(v)
                if len(res) == k:
                    return res
                

"""
Approach 2: Using a heap

"""

        
            


