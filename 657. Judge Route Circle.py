class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mov = {"U":1, "D":-1, "R":0.5, "L":-0.5}
        
        return not bool(sum(mov[i] for i in moves))
        
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