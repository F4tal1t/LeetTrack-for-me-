class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Brute Force
        '''
        time = 0
        while True:
            for i in range(len(tickets)):
                if tickets[k]==0:
                    return time
                if tickets[i] ==0:
                    continue
                if tickets[i]>=1:
                    tickets[i]-=1
                    time+=1
        '''
        # Optimized Approach
        result = 0
        for i in range(len(tickets)):
            if i<=k:
                result += min(tickets[i],tickets[k])
            else:
                result += min(tickets[i],tickets[k]-1)
        return result
