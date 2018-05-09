class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start = 0
        split = S.rfind(S[0])
        n=0
        result = []
        
        while n<len(S)-1:
            if S.find(S[n], split) > 0:
                split = S.rfind(S[n])
            if n == split:
                result.append(n+1-start)
                start=n+1
                split = S.rfind(S[start])
            n += 1
        
        result.append(len(S)-sum(result))
            
        return result
'''
Best Solutions
1.
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lst = {}
        n = len(S)
        for i,c in enumerate(S):
          lst[c] = i;
        ans = []
        max = 0
        pre = -1
        for i in range(n):
          if lst[S[i]] > max :
            max = lst[S[i]]
          if max == i :
            ans.append(max-pre)
            pre = max
            max = max+1
        
        return ans
		
2.
def partitionLabels(self, S):
    sizes = []
    while S:
        i = 1
        while set(S[:i]) & set(S[i:]):
            i += 1
        sizes.append(i)
        S = S[i:]
    return sizes
'''

'''
Notes
1. usage of set(), when comparing whether two list have a same element we can use set(a) & set(b)
2. try not to use while(), try to use for loop and iterator 