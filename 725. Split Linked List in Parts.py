class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        p = root
        length = 0
        
        while p:
            length += 1
            p = p.next
        
        num = [length//k for n in range(k)]
        mod = length%k
        for i in range(mod):
            num[i] +=1
        
        p = root
        a, b = 0, 0
        L = [p]
        
        
        while p:

            if a == num[b] - 1 and p.next is not None :
                b += 1
                L.append(p.next)
                p.next = None
                p = L[b]
                a = 0
            else:
                a += 1
                p = p.next
        
        while b < k-1:
            b += 1
            L.append(None)

        return L
		

'''
Best Solutions
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        n = 0
        ans = []
        while node:
            n += 1
            node = node.next
        num, rest = divmod(n, k)
        cur = root
        for i in range(k):
            head = cur
            for j in range(num + (i < rest) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
'''

'''
Notes
1. The choice of the loop body is a key factor in determining the time complexity. Take care whether to loop in linked list or in array

'''