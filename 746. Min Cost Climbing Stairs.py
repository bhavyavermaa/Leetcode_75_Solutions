class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b=cost[0],cost[1]
        for i in range(2,len(cost)):
            nxt=min(a,b)+cost[i]
            a,b=b,nxt
        return min(a,b)