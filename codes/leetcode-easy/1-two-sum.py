# Brute Force: O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
             
            
# Using dictionary: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for key, value in enumerate(nums):
            if (target - value) in nums_dict:
                return [nums_dict[target-value], key]
            else:
                nums_dict[value] = key
                
