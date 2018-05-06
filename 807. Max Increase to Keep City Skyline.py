def maxIncreaseKeepingSkyline(self, grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	num=0
	for i in range(1,4):
		for j in range(1,4):
			num+=min(max(grid[i]),max([x[j] for x in grid]))-grid[i][j]
	return num

		
'''
Best Solutions
1.
 def maxIncreaseKeepingSkyline(self, grid):
        row, col = map(max, grid), map(max, zip(*grid))
        return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))
'''

'''
Notes
1. map() is always faster than for loop. Attention that map() is an iterable objects so we need to use list(map()) to generate and display all results
2. for x in iterable objects, it will call for 'iter(iterable objects)' to generate a iterator with a method .__next__() in each loop to change x.
3. usage of zip() and zip(*):