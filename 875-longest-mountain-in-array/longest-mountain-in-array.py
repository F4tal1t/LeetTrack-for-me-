class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ret = 0 
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]: # Finds the Peak where both left and right are strictly decreasing
                l=r=i
                while l>0 and arr[l]>arr[l-1]: # Moves further down left if decreasing
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]: # Moves Further down right if decreasing
                    r+=1
                ret = max(ret,(r-l+1)) # r-l+1 indicates the range of the mountain
        return ret

