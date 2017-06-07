# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        first = cur = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 当某一个队列结束时，说明另一个队列剩下的都是较大的数，可以直接拼接至列表尾部
        cur.next = l1 or l2
        return first.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node3.next = node4

solution = Solution()
nodeFinal = solution.mergeTwoLists(node1,node3)
while nodeFinal:
    print(nodeFinal.val)
    nodeFinal = nodeFinal.next
