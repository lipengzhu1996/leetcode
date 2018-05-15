class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = [i for i in range(len(S)) if S[i] == C]
        a = []
        [a.append(min([abs(k-i) for k in pos])) for i in range(len(S))]
        
        return a
'''
Best Solutions

'''

'''
Notes
'''