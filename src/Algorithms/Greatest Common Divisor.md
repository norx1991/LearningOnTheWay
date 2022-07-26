### Euclidean algorithm (The time complexity of this algorithm is [O(log(min(a, b))](https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm/))

```python
 def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
```