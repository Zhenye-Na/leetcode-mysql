# 82. Single Number

- **Description**
    - Given `2 * n + 1` numbers, every numbers occurs twice except one, find it.
- **Example**
    - Given `[1,2,2,1,3,4,3]`, return `4`
- **Challenge**
    - One-pass, constant extra space.


## Solution

### `XOR` Operator

```java
a ^ b ^ b = a // 对一个数异或两次等价于没有任何操作！
```

因为只有一个数恰好出现一个，剩下的都出现过两次，所以只要将所有的数异或起来，就可以得到唯一的那个数，因为相同的数出现的两次，异或两次等价于没有任何操作！

- O(n) Time
- O(1) Space

```java
public class Solution {
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumber(int[] A) {
        // write your code here
        int result = 0, n = A.length;
        for (int i = 0; i < n; i++) {
            result ^= A[i];
        }
        return result;
    }
}
```

### Python `collections.Counter()`

- O(n) Time (at least) [`collections.Counter()` also sort the `keys` based on `values`]
- O(n) Space

```python
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        dict = collections.Counter(A)
        for key in dict:
            if dict[key] == 1:
                return key
```
