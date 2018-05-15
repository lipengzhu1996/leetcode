class StackUnderflow(ValueError):
	pass

class SStack():
	def __init__(self):
		self._elems = []

	def is_empty(self):
		return self._elems == []

	def top(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]

	def push(self, elem):
		self._elems.append(elem)

	def pop(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.pop()")
		return self._elems.pop()

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        operators = '+DC'
        
        stk = SStack()
        num = 0

        for c in ops:
            
            if c not in operators:
                stk.push(int(c))
                continue
            if c == 'C':
                stk.pop()
            elif c == 'D':
                stk.push(2*stk.top())
            elif c == '+':
                a = stk.pop()
                b = stk.pop()
                stk.push(b)
                stk.push(a)
                stk.push(a+b)
            else:
                break
                
        while not stk.is_empty():
            num += stk.pop()
        
        return num
'''
Best Solutions

'''

'''
Notes
'''