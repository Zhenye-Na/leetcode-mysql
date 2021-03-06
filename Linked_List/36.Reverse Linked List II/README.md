# 36. Reverse Linked List II

**Description**

Reverse a linked list from position `m` to `n`.

Given `m`, `n` satisfy the following condition: `1 <= m <= n <= length of list`.

**Example**

Example 1:

```
Input: 1->2->3->4->5->NULL, m = 2 and n = 4, 
Output: 1->4->3->2->5->NULL.
```

Example 2:

```
Input: 1->2->3->4->NULL, m = 2 and n = 3, 
Output: 1->3->2->4->NULL.
```

**Challenge**

Reverse it in-place and in one-pass


一道和 **dummy node** 有关的题目，要求把 `[m,n]` 之间的 nodes reverse，但是其实一共有 `(m-n+1)` 个点的 next 发生了变化。注意 reverse 结束后将 LinkedList 重新拼好。

```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or n < m or m < 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        count = 1
        prev, first = head, head.next
        while head.next and count < m:

            prev  = first
            first = first.next

            count += 1

        # first -> the m_th node in the LinkedList
        newLast  = first
        newFirst = prev

        switch = 0
        while switch <= n - m:
            tmp = first.next
            first.next = prev
            prev  = first
            first = tmp

            switch += 1

        newLast.next  = first
        newFirst.next = prev

        return dummy.next
```
