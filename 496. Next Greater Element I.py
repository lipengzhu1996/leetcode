class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        stk = []
        a=[]

        for i in nums:
            while len(stk) and stk[-1] < i:
                d[stk.pop()] = i
            stk.append(i)

        for j in findNums:
            a.append(d.get(j,-1))

        return a

'''
Best Solutions

'''

'''
Notes
'''