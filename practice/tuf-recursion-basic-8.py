class Solution:
    def fib(self, n):
        #your code goes here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

n = 6
print(Solution().fib(n))  