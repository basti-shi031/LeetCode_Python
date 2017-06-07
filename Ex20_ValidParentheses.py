class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1 = {"{": "}", "(": ")", "[": "]"}
        dict2 = {"}": "{", ")": "(", "]": "["}
        symbolStack = []
        for ch in s:
            if ch in dict1:
                symbolStack.append(ch)
            elif ch in dict2:
                if len(symbolStack) == 0:
                    return False
                popCh = symbolStack.pop()
                if popCh != dict2.get(ch):
                    return False
        if len(symbolStack) != 0:
            return False
        return True

solution = Solution()
print(solution.isValid("{}}"))