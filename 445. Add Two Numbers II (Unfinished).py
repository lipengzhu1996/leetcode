#To be continue...
#Unfinished

class ListNode(object):
        def __init__(self, x):
                self.val = x
                self.next = None

a = [9,9,9,9]
b = [1]

n1, n2 = 0, 0

head1 = ListNode(a[0])
p1 = head1

for i in a[1:]:
        p1.next = ListNode(i)
        p1 = p1.next

head2 = ListNode(b[0])
p2 = head2

for i in b[1:]:
        p2.next = ListNode(i)
        p2 = p2.next

l1 = head1
l2 = head2

while l1:
        n1 += 1
        l1 = l1.next

while l2:
        n2 += 1
        l2 = l2.next

n = 0

if n1 > n2:
        ll, ls = head1, head2
else:
        ll, ls = head2, head1

prev = ListNode(0)
prev.next = ll
l = prev
        
while ll:
        
        if n < abs(n2 - n1):
                n += 1
                prev = ll
                ll = ll.next
                continue
        
        num = ll.val+ls.val
        ll.val = num%10
        
        if num == 9 and ll.next and ls.next:
                if ll.next.val + ls.next.val >= 10:
                        prev.val += 1
                        ll.val = 0
        if num >= 10:
                prev.val += 1

        prev = ll      
        ll = ll.next
        ls = ls.next

if l.val == 0:
        l = l.next
