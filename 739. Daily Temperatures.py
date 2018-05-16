class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        d = {}
        stk = []
        a=[0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stk) and stk[-1][0] < temperatures[i]:
                [tem, day] = stk.pop()
                a[day] = i - day

            stk.append([temperatures[i], i])
        
        return a

'''
Best Solutions
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        jumper = [-1] * len(temperatures)
        result = [0] * len(temperatures)
        for i in xrange(len(temperatures) - 2, -1, -1):
            pos = i+1
            while pos != -1 and temperatures[i] >= temperatures[pos]:
                pos = jumper[pos]
            if pos == -1:
                result[i] = 0
            else:
                jumper[i] = pos
                result[i] = pos - i
        return result

'''

'''
Notes
'''