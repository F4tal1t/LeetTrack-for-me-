
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0 , len(nums)-1
        res = collections.deque()
        while l<=r:
            left , right = abs(nums[l]), abs(nums[r])
            if left > right:
                res.appendleft(left*left)
                l+=1
            else:
                res.appendleft(right*right)
                r-=1
        return list(res)