class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum, max_so_far = 0, -inf
        for num in nums:
            max_sum = max(num, max_sum + num)
            max_so_far = max(max_so_far, max_sum)
        return max_so_far
      
      
# Dynamic Programming

