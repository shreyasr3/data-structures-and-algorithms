# Space Complexity O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) != len(nums_set):
            return True
        else:
            return False
       
# Time Complexity O(n) , Space O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        else:
            return False
        
