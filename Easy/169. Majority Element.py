class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        times=l//2
        dict={}

        for i in range(l):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else: # if the key does not exist
                dict[nums[i]]=1
        
        majority=0
        for key in dict:
            if dict[key]>times:
                majority=key
                break
        
        return majority