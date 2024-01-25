class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # specila cases
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                                "CCCC").replace("CM", "DCCCC")

        for i in s:
            number = number + m[i]
        return number

x = Solution()
print(x.romanToInt("III"))
