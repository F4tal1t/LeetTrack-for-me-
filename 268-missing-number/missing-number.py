class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        # Unoptimised Approach
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            else:
                continue

        # nlogn approach using enumerate
        nums.sort()
        for i, v in enumerate(nums):
            if (i != v):
                return v-1
            if v == len(nums)-1:
                return v+1
        
        '''

        # Optimized Approach
        return sum(range(len(nums)+1)) - sum(nums)