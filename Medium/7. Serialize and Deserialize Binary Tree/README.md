# 7. Serialize and Deserialize Binary Tree

- **Description**
    - Design an algorithm and write code to serialize and deserialize a binary tree.
        - Writing the tree to a file is called 'serialization'.
        - Reading back from the file to reconstruct the exact same binary tree is 'deserialization'.
    - There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.
- **Example**
    - An example of testdata: Binary tree `{3,9,20,#,#,15,7}`, denote the following structure:

    ```
      3
     / \
    9  20
      /  \
     15   7
    ```

    - Our data serialization use BFS traversal. This is just for when you got wrong answer and want to debug the input.
    - You can use other method to do serializaiton and deserialization.

## Solution

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here

        if root is None:
            return "{}"

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(node)
            else:
                result.append(None)
            if not node:
                continue
            queue.append(node.left)
            queue.append(node.right)

        while True:
            if result[-1] is None:
                result.pop()
            else:
                break

        serialization = "{"
        serialization = serialization + str(result[0].val)


        for i in xrange(1, len(result)):
            if result[i] is not None:
                serialization = serialization + "," + str(result[i].val)
            else:
                serialization = serialization + ",#"

        return serialization + "}"



    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here

        if data == "{}":
            return None

        data = data[1:len(data)-1].split(",")
        root = TreeNode(int(data[0]))

        flag, parent = 1, 0
        nodeList = [root]

        for i in xrange(1, len(data)):

            if data[i] != "#":
                newNode = TreeNode(int(data[i]))

                if flag % 2 == 1:
                    nodeList[parent].left  = newNode
                    flag += 1
                else:
                    nodeList[parent].right = newNode
                    flag += 1

                nodeList.append(newNode)
            else:
                flag += 1

            if flag % 2 == 1:
                parent += 1


        return root
```
