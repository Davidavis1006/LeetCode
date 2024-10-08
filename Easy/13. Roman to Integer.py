class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_int=[]
        l=len(s)

        # convert symbols to integers
        for i in range(l):
            if s[i]=='I':
                s_int.append(1)
            elif s[i]=='V':
                s_int.append(5)
            elif s[i]=='X':
                s_int.append(10)
            elif s[i]=='L':
                s_int.append(50)
            elif s[i]=='C':
                s_int.append(100)
            elif s[i]=='D':
                s_int.append(500)
            elif s[i]=='M':
                s_int.append(1000)

        # sum up one by one and check for the subtraction instance
        num=0
        i=0
        while i<l-1:
            if s_int[i]>=s_int[i+1]:
                num+=s_int[i]
                i+=1
            else:
                num+=(s_int[i+1]-s_int[i])
                i+=2
        
        # add the last integer if it's not the subtraction instance
        if i==l-1:
            num+=s_int[i]

        return num