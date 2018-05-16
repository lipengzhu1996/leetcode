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

'''

'''
Notes
'''