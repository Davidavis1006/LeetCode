class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)

        i=0
        j=1
        while True:
            # scanning from i+1, search for the 1st element != nums[i]
            while j<=l-1 and nums[j]==nums[i]:
                j+=1
            
            if j==l:
                break

            # swap nums[i+1] and nums[j]
            temp=nums[i+1]
            nums[i+1]=nums[j]
            nums[j]=temp

            i+=1 # move forward to next target
            j+=1 # move forward to next starting point of search
        
        return i+1