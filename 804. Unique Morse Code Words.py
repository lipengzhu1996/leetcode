class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        src = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = []      
        for i in words:
            morse = ''
            for c in i:
                morse += src[ord(c) - ord('a')]
            code.append(morse)
        return len(set(code))
		
'''
Notes
1.for all nested for loop we can use list resolution to make it more concise, for eg.:
len({''.join(d[ord(i) - ord('a')] for i in w) for w in words}) equals to

x = set()
for w in words:
	str = ''
	for i in w:
		str=str.join(d[ord(i) - ord('a')])
	x.add(str)
len(x)

2.usage of set: filter duplicated elements
3.difference between set and dictionary