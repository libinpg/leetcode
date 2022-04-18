# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
import math
class Solution(object):
    #检查链表
    def checkListNode(self, l):
        ret = []
        while l!= None:
            ret.append(l.val)
            l = l.next
        return ret
    #构造链表
    def setListNode(self, array):
        l = ListNode(array[0], None)
        ret = l
        for i in range(1,len(array)):
            l.next = ListNode(array[i], None)
            l = l.next
        return ret
    #获取节点个数
    def getNodeCount(self, ListNode):
        nodeCount = 1
        while ListNode.next != None:
            nodeCount += 1
            ListNode=ListNode.next
        return nodeCount
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lengthOfl1 = lengthOfl2 = 0
        #保存l1,l2的指针
        templ1=l1
        templ2=l2
        #获取l1的节点个数
        lengthOfl1 = self.getNodeCount(templ1)
        #获取l2的节点个数
        lengthOfl2 = self.getNodeCount(templ2)
        #print(self.getNodeCount(l1))
        #print(self.getNodeCount(l2))
        #给位数少的补零节点
        if lengthOfl1 < lengthOfl2:
            templ1 = l1
            #将templ1指针移动到末尾
            while templ1.next != None:
                templ1 = templ1.next
            #在链表末尾加零节点
            for i in range(lengthOfl2 - lengthOfl1):
                templ1.next = ListNode(0 ,None)
                templ1 = templ1.next
        if lengthOfl1 > lengthOfl2:
            templ2 = l2
            #将templ1指针移动到末尾
            while templ2.next != None:
                templ2 = templ2.next
            #在链表末尾加零节点
            #print("l2-l1="+str(lengthOfl1 - lengthOfl2))
            for i in range(lengthOfl1 - lengthOfl2):
                print("二")
                templ2.next = ListNode(0 ,None)
                templ2 = templ2.next
        print(self.getNodeCount(l1))
        print(self.getNodeCount(l2))
        templ1 = l1
        templ2 = l2
        add = 0
        retNodeList = ListNode((l1.val+l2.val + add) % 10, None)
        if(l1.val + l2.val + add>= 10):
                add = 1
        else:
                add = 0
        l1 = l1.next
        l2 = l2.next
        temp = retNodeList
        while l1 != None or add != 0:
            try:
                retNodeList.next =  ListNode((l1.val+l2.val + add)%10, None)
                if(l1.val + l2.val + add>= 10):
                    add = 1
                else:
                    add = 0
                l1 = l1.next
                l2 = l2.next
            except:
                retNodeList.next =  ListNode(add, None)
                add = 0
            retNodeList = retNodeList.next
        #print(self.checkListNode(templ1))
        #print(self.checkListNode(templ2))
        #print(self.checkListNode(temp))
        return temp                                                                                                                                                                                                                                                                                                                                                                                                                                                         
a = [9,9,9,9,9,9,9]
b = [9,9,9,9]
s = Solution()
#构造li链表
l1 = s.setListNode(a)
l2 = s.setListNode(b)
print(s.addTwoNumbers(l1, l2))




print(Solution().addTwoNumbers(l1, l2))
