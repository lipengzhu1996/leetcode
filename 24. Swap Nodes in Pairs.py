class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        p0 = prev = ListNode(0)
        prev.next = curr = head

        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev = curr
            curr = curr.next
            
        return p0.next
		
'''

'''


'''
Best Solutions

'''

'''
Notes
'''