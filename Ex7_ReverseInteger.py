class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = x >= 0
        fixed_x = abs(x)
        str_x = str(fixed_x)
        result_x = str_x[::-1]
        print(result_x)
        print(fixed_x < 2 ** 31)
        result = int(result_x if positive else '-' + result_x)
        print(result)
        return result * (fixed_x < 0x7FFFFFFF and abs(result) < 0x7FFFFFFF)


solution = Solution()
print(solution.reverse(-1563847412))
print(2 ** 31)
