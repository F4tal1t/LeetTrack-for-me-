class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic Programming Approach
        '''
        dp = [0]* len(nums)
        for i, n in enumerate(nums):
            dp[i]=max(dp[i],dp[i-1]+n)
        return max(dp)
        '''

        # Normal Approach
        maxSum = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSum = max(maxSum, currentSum)
        return maxSum