class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        p={}
        n=0
        count=[]

        for i in cpdomains:
            key = []
            l = i.split(' ')
            num = int(l[0])
            t = l[1].count('.')
            for i in range (t+1):
                key.append(l[1].split('.',i)[-1])
            for k in key:
                if k in p.keys():
                    p[k] += num
                else:
                    p[k] = num

        for i in p:
            count.append(str(p[i])+' '+i)
            
        return count
'''
Best Solutions

'''

'''
Notes
'''