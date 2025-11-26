class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        One Liner 
        return heapq.nlargest(k,nums)[-1]
        
        Neap of N size , pop k
        stack = []
        for i in range(len(nums)):
            heapq.heappush(heap,i)
        for i in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        '''
        # Create  a min-heap with the first k elements
        heap = nums[:k]
        heapq.heapify(heap) # Time Complexity : O(k)

        # Iterate through the remaining elements
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap,num) # Time complexity: O((n-k) * 2log k) 
        
        return heap[0] # 0[1]

