#Timsort

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
        
        
#O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None for _ in nums]
        left, right = 0, len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        return result
