# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        循环遍历链表, 找到val对应的节点,将前结点尾指针与后结点头指针相连接
        """
        if head == None:
            return None
        ret = head
        last = head
        while head.val == val:
            if head.next == None:
                return None
            head = head.next
            ret = head   
        while head.next != None:
            last = head
            head = head.next
            if head.val == val:
                last.next = head.next
        return ret    
#head = [1,2,6,3,4,5,6];val = 6
head = [1,2,2,1];val = 2
#构建链表
l = ListNode(head[0])
h = l
for i in range(1, len(head)):
    temp = ListNode(head[i])
    l.next = temp
    l = l.next
l.next = None
print(Solution().removeElements(h, val))
#打印链表信息
l = Solution().removeElements(h, val)
while l != None:
    print(l.val)
    l = l.next