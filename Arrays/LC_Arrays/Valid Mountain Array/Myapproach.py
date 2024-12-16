class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Understand
        input: array of int (any size)
        output: t or f
        goal: check if it is a valid mountain array.
        To be a valid mountain array: every val upto arr[i] is strictly increasing and every val after arr[i] is decreasing. Arr.len is 3>
        Task:
        check if arr.len 3+
        iterate once to get the max of the array
        set decreasing = f
        for i in range(1,len(arr)):
            if arr[i] = max
                decreasing = t
            if decreasing == f:
                if arr[i] <= arr[i-1]:
                    return f
            else:
                if arr[i] >= arr[i-1]
                    return f
        return t

        """
        decreasing = False
        if len(arr) < 3:
            return False
        max = arr[0]
        for i in arr:
            if i > max:
                max = i
        if max == arr[len(arr) -1] or max == arr[0]:#no ddecreasing section
            return False

        for idx in range(1,len(arr)):
            
            if decreasing == False:
                if arr[idx] <= arr[idx-1]:
                    return False
                if arr[idx] == max:
                    decreasing = True
            else:
                if arr[idx] >= arr[idx-1]:
                    return False
        return True

         