# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultFirstNode = resultNode = ListNode(0)
        addMoreTen = False
        while l1 or l2 or addMoreTen:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            result = v1 + v2 + (1 if addMoreTen else 0)
            addMoreTen = result >= 10
            result = result % 10
            resultNode.next = ListNode(result)
            resultNode = resultNode.next
        return resultFirstNode.next


solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(7)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

result = solution.addTwoNumbers(node1, node4)
while result:
    print(result.val)
    result = result.next
