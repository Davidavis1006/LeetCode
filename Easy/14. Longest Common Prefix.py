class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # since O(WL) for creating a Trie, use naive instead 

        l=len(strs)

        if l==1:
            return strs[0]

        # find the minimum sting length
        min_str_l=len(strs[0])
        for i in range(1, l):
            if len(strs[i])<min_str_l:
                min_str_l=len(strs[i])
        
        lcp=""
        exit_flag=False
        for i in range(min_str_l): # for the ith letter
            ch=strs[0][i]
            for j in range(1, l): # for each string
                if strs[j][i]!=ch:
                    exit_flag=True
                    break
            
            if exit_flag:
                break

            lcp+=ch # update prefix

        return lcp