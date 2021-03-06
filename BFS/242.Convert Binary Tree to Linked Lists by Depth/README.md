# 242. Convert Binary Tree to Linked Lists by Depth

**Description**

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

**Example**

Example 1:

```
Input: {1,2,3,4}
Output: [1->null,2->3->null,4->null]
Explanation: 
        1
       / \
      2   3
     /
    4
```

Example 2:

```
Input: {1,#,2,3}
Output: [1->null,2->null,3->null]
Explanation: 
    1
     \
      2
     /
    3
```


**BFS**

```python
from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        nodeList = []
        if root is None:
            return nodeList

        queue = deque([])
        queue.append(root)

        while queue:
            first = ListNode(0)
            dummy = first
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                newlistNode = ListNode(node.val)
                first.next = newlistNode
                first = newlistNode

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            nodeList.append(dummy.next)

        return nodeList
```


**DFS**


```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        result = []
        self.dfs(root, 1, result)
        return result

    def dfs(self, root, depth, result):
        if root is None:
            return

        node = ListNode(root.val)
        if len(result) < depth:
            result.append(node)
        else:
            node.next = result[depth - 1]
            result[depth - 1] = node
        
        self.dfs(root.right, depth + 1, result)
        self.dfs(root.left, depth + 1, result)
```
