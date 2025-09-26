class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        index = len(s)-1
        output = ""
        return self.helper(s,output,index)
    
    def helper(self,s,output,index):
        if index < 0:
            return s == output 
        
        ch = s[index]
        output += ch

        return self.helper(s,output,index-1)
    
s = "aaabbaaa"
print(Solution().palindromeCheck(s))
