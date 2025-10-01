class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans ,sol =[],[]
        def backtrack(x):
            if len(sol)==k:
                ans.append(sol[:])
                return
            left = x
            stillNeeded = k - len(sol)
            if left > stillNeeded:
                backtrack(x-1)
            sol.append(x)
            backtrack(x-1)
            sol.pop()
        backtrack(n)
        return ans