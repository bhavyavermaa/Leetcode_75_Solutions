class Solution:
    def helper(self, m: int, n: int) -> int:
        prev = [0] * (n+1)
        for i in range(m+1):
            temp = [0] * (n+1)
            for j in range(n+1):
                if i < 1 or j < 1:
                    temp[j] = 1
                else:
                    temp[j] = prev[j] + temp[j-1]
            prev = temp
        return prev[n]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(m-1, n-1)