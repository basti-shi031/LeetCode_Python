import time
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 时间 O(n)
        # 空间 O(n)
        x_str = str(x)
        length = len(x_str)
        middle_index = int(length / 2)
        for index in range(0, middle_index):
            if x_str[index] != x_str[-1 - index]:
                return False
        return True

    def isPalindrome2(self, x):
        # 时间 O(n)
        # 空间 O(1)
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p /= 10
        return res == x


solution = Solution()
start1 = time.time()
print(solution.isPalindrome(123321))
print(solution.isPalindrome2(123321))