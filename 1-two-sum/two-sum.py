class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bruh={}
        for i,n in enumerate(nums):
            diff= target-n
            if diff in bruh:
                return [bruh[diff],i]
            bruh[n]=i