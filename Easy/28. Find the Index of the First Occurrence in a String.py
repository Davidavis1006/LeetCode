class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=len(needle)

        for i in range(len(haystack)-l+1):
            substr=haystack[i:i+l]

            if substr==needle:
                return i
            
        return -1