class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        '''
        Set Method
        s=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False
        '''
        # Optimised One
        if len(set(nums)) == len(nums):
            return False
        else:
            return True