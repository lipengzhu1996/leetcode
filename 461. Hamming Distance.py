class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s1 = str(bin(x))[2:]
        s2 = str(bin(y))[2:]
        
        length = max(len(s1),len(s2))
        
        s1 = s1.zfill(length)
        s2 = s2.zfill(length)
        
        a = 0
        
        return len([a for i in range(length) if not s1[i] == s2[i]])
'''
Best Solutions
1.
return bin(x^y).count('1')
'''

'''
Notes
1. usage of ^ which means XOR in python