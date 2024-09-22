class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0 # pointer for nums1
        j=0 # pointer for nums2
        mergeArray=[]

        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                mergeArray.append(nums1[i])
                i+=1
            else:
                mergeArray.append(nums2[j])
                j+=1

        while (i<m):
            mergeArray.append(nums1[i])
            i+=1

        while (j<n):
            mergeArray.append(nums2[j])
            j+=1

        nums1[:]=mergeArray # assign in-place