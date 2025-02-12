class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

# Main program
if __name__ == '__main__':
    print("Enter the elements (one per line):")
    nums = []
    for i in range(4):
        nums.append(int(input()))
    
    print("Enter the target sum:")
    target = int(input())
    
    print("Numbers:", nums)
    print("Target:", target)
    
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Result:", result)