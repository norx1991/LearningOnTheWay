```python
def subsets(nums):
    """
    :param nums: values to select from
    :return: all subsets

    >>> print(subsets([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    output, cur = [], []

    def backtrack(start):
        output.append(cur[:])

        for i in range(start, len(nums)):
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()

    backtrack(0)
    return output

# Another method
def subsets2(nums):
    """
    :param nums: values to select from
    :return: all subsets

    >>> print(subsets([1, 2, 3]))
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    res = [[]]
    for num in nums:
        res.extend([x + [num] for x in res])
    return res


def subsetsWithDup(nums):
    """
    :param nums: values to select from. Allow duplication
    :return: all unique subsets

    >>> print(subsetsWithDup([1, 2, 3, 3]))
    [[], [3], [3, 3], [2], [2, 3], [2, 3, 3], [1], [1, 3], [1, 3, 3], [1, 2], [1, 2, 3], [1, 2, 3, 3]]
    """
    from collections import Counter
    ct = Counter(nums)

    output, cur = [], []

    items = list(ct.items())

    def backtrack(idx):
        k, v = items[idx]
        for i in range(v + 1):
            cur.extend([k] * i)

            if idx == len(items) - 1:
                output.append(cur[:])

            if idx < len(items) - 1:
                backtrack(idx + 1)

            for _ in range(i):
                cur.pop()

    backtrack(0)
    return output
```
