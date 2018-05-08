class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        num = []
        
        for x in range(left, right+1):
            if not sum(x%i for i in [int(i) for i in str(x)] if not i == 0):
                if not str(x).count('0'):
                    num.append(x)
   
        return num

#       [num.append(x) for x in range(left, right+1) if not sum(x%i for i in [int(i) for i in str(x)] if not i == 0 if not str(x).count('0')]

'''
Best Solutions
1.
return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
'''

'''
Notes
1.
fool
'''