class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split() # leading and trailing whitespaces are ignored in the returned list
        
        return len(words[-1])