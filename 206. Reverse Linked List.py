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