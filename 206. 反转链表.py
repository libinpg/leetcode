# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        ret = ListNode(head.val)
        while head.next != None:
            head = head.next
            temp = ListNode(head.val)
            temp.next = ret
            ret = temp
        return ret
head = [1,2,3,4,5]
#构建链表
l = ListNode(head[0])
h = l
for i in range(1, len(head)):
    temp = ListNode(head[i])
    l.next = temp
    l = l.next
print(Solution().reverseList(h))