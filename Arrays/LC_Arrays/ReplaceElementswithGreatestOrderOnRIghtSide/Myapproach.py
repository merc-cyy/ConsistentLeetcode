class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #input: arr of int
        #output: arr of int
        #goal: replace every val with the greatest element on the right side of    the array except the last one, replace with -1
        #limits: arr.len > 1 and arr[i] is always an int

        #steps: for every val, find the max of the right side, replace element with val--0(n2); except for when last val then replace with -1(Brute force)
        #optimized_steps; iterate from the right to left, start with max of -1, if val is bigger, replace max.
        #edge: arr has one element, all the same element 
        max_val = -1
        n = len(arr)
        for idx in range(n-1, -1, -1):
                temp = arr[idx]
                arr[idx] = max_val
                max_val = max(temp, max_val)

        return arr 


        