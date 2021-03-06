# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for firstIndex in range(0, len(nums) - 2):
            secondIndex = firstIndex + 1
            thirdIndex = len(nums) - 1
            while secondIndex < thirdIndex:
                sum = nums[firstIndex] + nums[secondIndex] + nums[thirdIndex]

                if target == sum:
                    return sum

                if abs(result - target) > abs(sum - target):
                    result = sum
                if target < sum:
                    thirdIndex -= 1
                if target > sum:
                    secondIndex += 1

        return result
