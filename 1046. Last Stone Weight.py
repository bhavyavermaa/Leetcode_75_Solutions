class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return sum(stones)
        while len(stones) > 1:
            stones = sorted(stones)[::-1]
            destroyed = stones[0] - stones[1]
            stones.append(destroyed)
            stones = stones[2:]
        return sum(stones)