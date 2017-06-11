# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if len(nums) < 3:
            return []

        nums.sort()
        for firstIndex in range(len(nums) - 2):
            if firstIndex>0 and nums[firstIndex] == nums[firstIndex-1]:
                # 去除同数字可能性
                continue
            secondIndex, thirdIndex = firstIndex + 1, len(nums) - 1
            while (secondIndex < thirdIndex):
                a = nums[firstIndex]
                b = nums[secondIndex]
                c = nums[thirdIndex]
                sum = nums[firstIndex] + nums[secondIndex] + nums[thirdIndex]
                if sum < 0:
                    secondIndex = secondIndex + 1
                elif sum > 0:
                    thirdIndex = thirdIndex - 1
                else:
                    result.append((nums[firstIndex], nums[secondIndex], nums[thirdIndex]))
                    while secondIndex < thirdIndex and nums[secondIndex] == nums[secondIndex + 1]:
                        secondIndex = secondIndex + 1
                    while secondIndex < thirdIndex and nums[thirdIndex] == nums[thirdIndex - 1]:
                        thirdIndex = thirdIndex - 1
                    secondIndex = secondIndex + 1
                    thirdIndex = thirdIndex - 1
        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
