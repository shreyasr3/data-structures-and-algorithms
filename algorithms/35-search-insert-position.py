class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) >> 1
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
      
      
      
      
      
      #Python library
      
class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)
     
        
