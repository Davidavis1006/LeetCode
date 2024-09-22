class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l=len(digits)

        if digits[l-1]!=9: # if last digit is not 9
            digits[l-1]+=1
        else: # last digit is 9
            if l==1:
                digits[0]=0
                digits.insert(0, 1)
            else:
                # for digits except the first
                for i in range(l-1, 0, -1):
                    digits[i-1]+=1
                    digits[i]=0
                    # stop if no consecutive 9s
                    if digits[i-1]!=10:
                        break

                # check for first digit
                if digits[0]==10:
                    digits[0]=0
                    digits.insert(0, 1)

        return digits