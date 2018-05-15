class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        p = head
        start = ListNode(head.val - 1)
        start.next = head

        while p and p.next:
            if p.next.val >= p.val:
                p = p.next
                continue

            l = start
            while l.next.val < p.next.val:
                l = l.next

            tmp = p.next
            p.next = tmp.next
            tmp.next = l.next
            l.next = tmp

        return start.next
'''
Best Solutions

'''

'''
Notes
'''