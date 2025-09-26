class Solution:
    def checkPrime(self, num):
        #your code goes here
        if num == 1 or num == 0: 
            return False
        x = num - 1
        return self.helper(num,x)
    
    def helper(self,num,x):
        if x <= 1:
            return True 
        if (num % x == 0):
            return False
        return self.helper(num,x-1)

num = 1
print(Solution().checkPrime(num))
