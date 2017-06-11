class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 1
        size = len(nums)
        if size == 1:
            return 1
        for index in range(1, size):

