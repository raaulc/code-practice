class Solution:
    def addDigits(self, num):
        #your code goes here
        if num < 10:
            return num
        
        digit_sum = sum(int(d) for d in str(num))
        return self.addDigits(digit_sum)



num = 499
print(Solution().addDigits(num))
