from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2,7,11,15], target=9))
    print(solution.twoSum(nums=[3,2,4], target=6))
    print(solution.twoSum(nums=[3,3], target=6))