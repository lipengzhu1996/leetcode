class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prevnode = None
        p = head

        
        while p:
            nextnode = p.next
            p.next = prevnode
            prevnode = p
            p = nextnode
            
        return prevnode
		
'''
Recursively:

class Solution(object):
    def reverseList(self, head, prev = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return prev
        
        curr = head.next
        head.next = prev
        return self.reverseList(curr, head)
'''