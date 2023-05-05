class Solution:
    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    def fib(self, n: int) -> int:
        return self.fibonacci(n)