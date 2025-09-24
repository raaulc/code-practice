from typing import List

def rob(self, nums: List[int]) -> int:
    index = 0
    ans = solve(nums,index)
    return ans

def solve(nums,index) -> int:
      #base case 
      if(index >= len(nums)):
           return 0
      
      #include
      include = nums[index]+solve(nums,index+2)
      #exclude
      exclude = 0 + solve(nums,index+1)
      return max(include,exclude)
