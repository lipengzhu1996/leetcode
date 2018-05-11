class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        setG = set(G)
        num=0
        
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                num += 1
            head = head.next
            
        return num
		
'''
TLE:
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        pos = []
        num = 1
        
        for i in G:
            p = head
            n=0
            while p is not None:
                if i == p.val:
                    pos.append(n)
                    break
                p= p.next
                n += 1
                
        pos.sort()

        for i in range(1,len(pos)):
            if not pos[i] - pos[i-1] == 1:
                num += 1
        
        return num
'''
'''
Best Solutions

'''

'''
Notes
'''