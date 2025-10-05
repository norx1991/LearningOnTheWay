```python
from typing import List


def permute(nums):
    """
    :param nums: values to be permuted
    :return: all permutations
    
    >>> print(permute([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """

    def backtrack(start):
        if start == n:
            output.append(nums[:])
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    n = len(nums)
    output = []
    backtrack(0)
    return output


def permuteUnique(nums):
    """
    :param nums: values to be permuted
    :return: all permutations

    >>> print(permuteUnique([1, 1, 2]))
    [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    >>> print(permuteUnique([1, 2, 3, 3]))
    [[1, 2, 3, 3], [1, 3, 2, 3], [1, 3, 3, 2], [2, 1, 3, 3], [2, 3, 1, 3], [2, 3, 3, 1], [3, 2, 1, 3], [3, 2, 3, 1], [3, 1, 2, 3], [3, 1, 3, 2], [3, 3, 1, 2], [3, 3, 2, 1]]

    """
    output = []

    def backtrack(start):
        if start == len(nums) - 1:
            output.append(nums[:])
            return

        seen = set()
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            nums[i], nums[start] = nums[start], nums[i]
            backtrack(start + 1)
            nums[i], nums[start] = nums[start], nums[i]

    backtrack(0)
    return output


# Another approach with Counter
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    from collections import Counter
    ct = Counter(nums)
    res = []

    def backtrack(cur, counter):
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        for c, count in counter.items():
            if count == 0:
                continue
            cur.append(c)
            counter[c] -= 1
            backtrack(cur, counter)
            counter[c] += 1
            cur.pop()

    backtrack([], ct)
    return res
```