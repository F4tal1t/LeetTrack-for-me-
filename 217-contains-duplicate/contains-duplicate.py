class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False