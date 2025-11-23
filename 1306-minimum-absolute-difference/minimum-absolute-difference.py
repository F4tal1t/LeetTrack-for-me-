class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbs = float('inf')
        # Finding the Absolute Difference
        for i in range(len(arr)):
            minAbs = min(minAbs, abs(arr[i]-arr[i-1]))
        
        res = []
        # Appending the list with the pairs
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == minAbs:
                res.append([arr[i-1],arr[i]])
        
        return res

