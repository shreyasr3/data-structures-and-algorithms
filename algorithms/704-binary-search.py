#O(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        for i in range(0,len(nums)):
            if target == nums[i]:
                return i
                break
        else:
            return -1

          
#O(logn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
