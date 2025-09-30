class Solution(object):
    def twoSum(self, nums, target):
        Pmap = {}
        for i, n in enumerate(nums):
            t=target-n
            if t in Pmap:
                return [Pmap[t], i]
            Pmap[n] = i
