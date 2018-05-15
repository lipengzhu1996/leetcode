class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        p = prev = head
        curr = head.next

        while curr:
            
            if curr.val == prev.val:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
                
            else:
                curr = curr.next
                prev = prev.next
        
        return p
'''

'''