# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        pointerarray = []
        while head.next != None:
            if head in pointerarray:
                return  True
            pointerarray.append(head)
            head = head.next
        return False
        #print(head.next.next.next.next.val)
head = [3,2,0,-4];pos = 1
#构建链表
l = ListNode(head[0])
h = l
pospointer = None
for i in range(1, len(head)):
    temp = ListNode(head[i])
    if i == pos:
        pospointer = temp
    l.next = temp
    l = l.next
l.next = pospointer
print(Solution().hasCycle(h))