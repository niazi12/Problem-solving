class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        s = strs[0]
        prefix = ""
        for i in range(len(s)):
            if strs[len(strs) - 1][i] == s[i]:
                prefix += strs[len(strs) - 1][i]
            else:
                break
        return prefix
