```python

def combine(nums, k):
    """
    :param nums: values to select from
    :param k: number of values to pick
    :return: combinations with k values from nums

    >>> print(combine([1, 2, 3], 2))
    [[1, 2], [1, 3], [2, 3]]
    >>> print(combine([1, 2, 3, 3], 2))
    [[1, 2], [1, 3], [1, 3], [2, 3], [2, 3], [3, 3]]
    """
    output, cur = [], []

    def backtrack(start):
        if len(cur) == k:
            output.append(cur[:])
            return
        for i in range(start, len(nums) + 1 - k + len(cur)):
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()

    backtrack(0)
    return output


def combineUnique(nums, k):
    """

    :param nums: values to select from, may have duplicate
    :param k: number of values to pick
    :return: combinations with k values from nums

    >>> print(combineUnique([1, 2, 3, 3], 2))
    [[3, 3], [2, 3], [1, 3], [1, 2]]
    """
    from collections import Counter
    ct = Counter(nums)

    output, cur = [], []

    items = list(ct.items())

    def backtrack(idx):
        if idx == len(items):
            return
        num, v = items[idx]
        for i in range(min(v + 1, k - len(cur) + 1)):
            cur.extend([num] * i)

            if len(cur) == k:
                output.append(cur[:])

            if len(cur) < k:
                backtrack(idx + 1)

            for _ in range(i):
                cur.pop()

    backtrack(0)
    return output


def combineWithRepetition(nums, k):
    """

    :param nums: values to select from
    :param k: number of values to pick
    :return: combinations with k values from nums. Each value can be selected any number of times

    >>> print(combineWithRepetition([1, 2, 3], 2))
    [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]]
    """
    output, cur = [], []

    def backtrack(start):
        if len(cur) == k:
            output.append(cur[:])
            return
        for i in range(start, len(nums)):
            cur.append(nums[i])
            backtrack(i)
            cur.pop()

    backtrack(0)
    return output
```
