class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)

        if l==0:
            return 0
        elif l==1:
            if nums[0]==val:
                return 0
            else:
                return 1

        i=0
        j=l-1
        while True:
            # scanning from left, search for val
            while i<=l-1 and nums[i]!=val:
                i+=1
            
            # scanning from right, search for non-val
            while j>=0 and nums[j]==val:
                j-=1
            
            if i>j:
                break
            
            # swap nums[i] and nums[j]
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        
        return j+1