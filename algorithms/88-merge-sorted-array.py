class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = m+n-1
        
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[res] = nums1[m-1]
                m -= 1
            else:
                nums1[res] = nums2[n-1]
                n -= 1
            
            res -= 1
            
            
