def intersect(seq1,seq2):
        res = []
        for x in seq1:
                if x in seq2:
                        res.append(x)
        return len(res)

'''
Best Solutions
1.
def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))

2.
def numJewelsInStones(self, J, S):
        return sum(map(S.count, J))

3.
def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)
'''

'''
Notes
1. usage of map(function, list): map for specified function according to given list
2. list.count(c): count the number of occurrences of c in list
3. sum(s in J for s in S) is equal to:
        for s in S:
            if s in J:
               res += 1
        ruturn res
	this is called list resolution
'''
