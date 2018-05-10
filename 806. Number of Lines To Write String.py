class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        n = 0
        line = 1
        
        for c in S:
            n += widths[ord(c) - ord('a')]
            if n > 100 :
                line += 1
                n = widths[ord(c) - ord('a')]
        
        return [line, n]

'''
Best Solutions

'''

'''
Notes

'''
