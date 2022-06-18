# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #print(list1.next.next.val)
        #print(list2.next.next.val)
        if list1 == None and list2 == None:
            return None
        if list1 != None and list2 == None:
            return list1
        if list2 != None and list1 == None:
            return list2
        ret = None
        if list1.val <= list2.val:
            ret = ListNode(list1.val)
            list1 = list1.next
        else:
            ret = ListNode(list2.val)
            list2 = list2.next
        r = ret
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                ret.next = ListNode(list1.val)
                ret = ret.next
                list1 = list1.next
            else:
                ret.next = ListNode(list2.val)
                ret = ret.next
                list2 = list2.next
        while list1 != None:
            ret.next = ListNode(list1.val)
            ret = ret.next
            list1 = list1.next
        while list2 != None:
            ret.next = ListNode(list2.val)
            ret = ret.next
            list2 = list2.next
        return r
        # while r != None:
        #     print(r.val)
        #     r = r.next
l1 = [1,2,4];l2 = [1,3,4]
list1 = ListNode(l1[0])
h1 = list1
for i in range(1, len(l1)):
    temp = ListNode(l1[i])
    list1.next = temp
    list1 = list1.next
list1.next = None
list2 = ListNode(l2[0])
h2 = list2
for i in range(1, len(l2)):
    temp = ListNode(l2[i])
    list2.next = temp
    list2 = list2.next
list2.next = None
print(Solution().mergeTwoLists(h1, h2))