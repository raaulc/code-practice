class Solution:
    def NnumbersSum(self, N):
        result = 0
        return self.helper(result,N)
    def helper(self,result,N):
        if N == 0:
            return result
        result = result + N
        return self.helper(result,N-1)
