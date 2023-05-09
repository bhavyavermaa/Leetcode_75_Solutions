class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        if n==1:
            return n
        for i in range(2,n):
            a,b=b,a+b
        return b
        