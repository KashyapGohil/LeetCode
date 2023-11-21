from typing import List

# Solution 1: (Brute Force)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

# Solution 2: (Two-pass Hash Table)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_lookup = {}
        # build the hash table
        for index in range(len(nums)):
            seen_lookup[nums[index]] = index

        # Fin the complement             
        for index in range(len(nums)):
            complement  = target - nums[index]
            if complement  in seen_lookup and seen_lookup[complement] != index:
                return [index, seen_lookup[complement ]]
        return [] # No solution found
       
# Solution 3: (One-pass Hash Table)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_lookup ={}

        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in seen_lookup:
                return [seen_lookup[complement], index]
            seen_lookup[nums[index]] = index
        return [] # No solution found

# Testing    
solution_object = Solution()
print(solution_object.twoSum([4,-2,5,0,6,3,2,7],1))
        