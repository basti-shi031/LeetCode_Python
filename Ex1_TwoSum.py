class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 思路：
        # 一个 dict, key 为值, value 为该值在 nums 中的 index
        # 对 nums 进行遍历,对每一个nums中的元素,如果 (target - num) 不存在于 dict 中, 说明没有找到需要的结果,就将 num 存在 dict中
        # 反之，如果 （target - num） 存在于 dict 中，说明之前某一个 num = （target - 当前的 num），即这两个数是满足要求的数

        #  遍历 nums ，复杂度为 O(n)


        contentDict = {}

        for index in range(0, len(nums)):
            if target - nums[index] in contentDict:
                return [contentDict[target - nums[index]], index]
            contentDict[nums[index]] = index


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
