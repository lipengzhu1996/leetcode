class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        odd = head
        even = head.next
        p = even

        while odd and even:
            
            if not even.next:
                even.next = None
                odd.next = p
                break
            odd.next = even.next
            odd = odd.next
            
            if not odd.next:
                even.next = None
                odd.next = p
                break
            even.next = odd.next
            even = even.next
        
        return head
'''
Best Solutions

'''

'''
Notes
'''