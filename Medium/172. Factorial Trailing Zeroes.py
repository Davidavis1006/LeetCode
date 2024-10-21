class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros=0
        base=5 # power of 5
        
        while base<=n:
            zeros+=n//base
            base*=5
        
        return zeros