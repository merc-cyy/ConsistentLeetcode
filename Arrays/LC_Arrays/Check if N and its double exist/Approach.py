class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Understand: input: arr of int
                    output: T or F
                    goal: check if a val n and its double exist in the array
                    task: 
                    dict
                    for i in array:
                        if i not in dict;
                            put i in dict and index
                            check if i*2 is in dict or i/2 in dict:
                                return true

                    return false

        """
        values = {}
        for idx in range(len(arr)):
            
            if (arr[idx] * 2 in values) or (arr[idx] / 2 in values):
                return True

            if arr[idx] not in values:
                values[arr[idx]] = idx
                
        return False
