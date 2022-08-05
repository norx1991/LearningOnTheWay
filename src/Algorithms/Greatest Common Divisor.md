### Euclidean algorithm (The time complexity of this algorithm is [O(log(min(a, b))](https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm/))

```python
 def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
```

### The least common multiple can be found by the following
```python
def lcm(a, b):
    return a * b // gcd(a, b)
```