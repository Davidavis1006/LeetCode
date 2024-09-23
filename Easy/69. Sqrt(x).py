class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x

        # binary search
        l=1
        r=x
        while l<r:
            mid=(l+r)//2

            if mid*mid==x:
                return mid
            elif mid*mid>x:
                r=mid-1
            elif mid*mid<x:
                l=mid+1

        if l*l==x: # few outliers
            return l
        elif l*l<x:
            return l # or r, since l==r now
        else:
            return l-1 # or r-1, since l==r now