class Solution(object):
    def myAtoi(self, num_str):
        """
        :type num_str: str
        :rtype: int
        """
        fixed_str = num_str.strip(" ")
        positive = True
        if fixed_str.startswith('-'):
            positive = False
            fixed_str = fixed_str[1:]
        if fixed_str.startswith('+'):
            positive = True
            fixed_str = fixed_str[1:]
        if not fixed_str.isdigit():
            return 0
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        num = 0
        for item in fixed_str:
            num = 10 * num + dict[item]
        return num if positive else -num


    def myAtoi2(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        # if len(ls) == 0 : return 0
        if len(s) == 0: return 0
        ls = list(s.strip())

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

solution = Solution()
print(solution.myAtoi2("-1"))
