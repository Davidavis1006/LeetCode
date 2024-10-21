class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # preprocessing
        s=list(s)

        for i in range(len(s)):
            if s[i].isalnum(): # a-z and 0-9
                s[i]=s[i].lower() # lower(): symbols and numbers are ignored
            else:
                s[i]=""
        
        s="".join(s)

        # check for palindrome
        if s==s[::-1]:
            return True
        else:
            return False