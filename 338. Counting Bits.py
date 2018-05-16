class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        n = 1
        s = []
        res = []

        while n <= num:
            s.append(n)
            n *= 2

        for i in range(num+1):
            k = 0
            for j in range(len(s), 0, -1):
                i -= s[j-1]
                if i > 0:
                    k += 1
                elif i == 0:
                    k += 1
                    break
                elif i < 0:
                    i += s[j-1]
            res.append(k)
            
        return res
'''
Best Solutions
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) < num + 1:
            ans += [1 + x for x in ans]
        # len(ans) > num
        return ans[:num+1]
'''

'''
Notes
'''