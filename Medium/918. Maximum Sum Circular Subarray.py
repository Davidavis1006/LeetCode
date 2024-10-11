class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find max_sum
        current_max=nums[0]
        global_max=nums[0]

        for i in range(1, len(nums)):
            current_max=max(nums[i], current_max+nums[i])

            if current_max>global_max:
                global_max=current_max
        
        # find min_sum
        current_min=nums[0]
        global_min=nums[0]

        for i in range(1, len(nums)):
            current_min=min(nums[i], current_min+nums[i])

            if current_min<global_min:
                global_min=current_min
        
        total_sum=sum(nums)

        if global_min==total_sum: # all negative
            return global_max
        else: # (a) Max Subarray in the middle, (b) Max Subarray split across
            return max(global_max, total_sum-global_min)