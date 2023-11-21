from typing import List 

# Solution 1: Brute Force- Merge and Sort
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the arrays into a single sorted array.
        merged_array = nums1 + nums2
        merged_array.sort()

        # calucaluting the len of merged array
        n = len(merged_array)

        if n % 2 != 0:
            return float(merged_array[n // 2])
        else:
            return float((merged_array[(n -1) // 2] + merged_array[n // 2]) / 2.0)


# Driver code & funtions call    
solution_object = Solution()
print(solution_object.findMedianSortedArrays([1,2],[3,4,5,6,7,8]))        