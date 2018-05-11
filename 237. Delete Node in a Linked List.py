class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
		

'''
Best Solutions

'''

'''
Notes
1. the concept of "delete a node" is kind of smart: you do not need to delete a node, you just need to remove it from the linked list chain.
'''