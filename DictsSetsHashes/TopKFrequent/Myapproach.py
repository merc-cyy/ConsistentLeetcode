class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input: array of int and int k
        #output: array of int
        #goal: return top k most freq elements
        #task: find the frequencies of all elements and return top k
        #steps: create a dict storing vals and their count
        #   iterate through the HT k times, removing the val with highest count up till k elements are removed or dict is empty


        val_dict = defaultdict(int)

        for i in nums:
            val_dict[i] += 1#create a dict with values and their count

        ans = []
        max_count = 0
        for j in range(k):
            max_key = max(val_dict, key=val_dict.get)
            ans.append(max_key)
            del val_dict[max_key]
            #iterate through the array removing k elements with highest count

        return ans[:k]
    
    #Time: O(n * k) where n is the size of input array and k is the number given
    #space: o(n) the hash table


