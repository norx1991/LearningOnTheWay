# deque 

from collections import deque

- append(x)
- appendleft(x)
- pop()
- popleft()
- clear()
- count()
- extend(iterable)
- extendleft()
- remove(val)
- reverse()
- rotate(n = 1)
- maxlen

# heapq

import heapq

- heappush(h, item)
- heappop(h)
- heapreplace(h, item)
- heapify(h)

# bisect

import bisect

- bisect(list, val, low=0, high=len(list))
- bisect_left(list, val)
- insort(list, val)
- insort_left(list, val)

# binary search tree
from sortedcontainers import SortedList (Similar to multiset in C++)

- add(val)
- update(iterable)
- discard(val)
- remove(val)
- pop(index=-1)
- count(val)
- index(val)
- bisect_left(val)
- bisect_right(val)

from sortedcontainers import SortedDict

- pop(key)
- popitem(index=-1)
- peekitem(index=- 1) (return (key, value) pair at index)
  
from sortedcontainers import SortedSet

- add(val)
- pop(index=-1)
- remove(val)
- discard(val)

# Useful Functions
- chr(97) = 'a'
- ord('a') = 97
- map(fun, iterable)
- filter(fun, iterable)
- reduce(func, iterable)
- float('inf')
- divmod()
- bin()
- float.is_integer()
- int.bit_length()

# Useful Syntax

- [f(x) if condition else g(x) for x in sequence]
- [f(x) for x in sequence if condition]
- [entry for tag in tags for entry in entries if tag in entry]
- dp = [[[0 for _ in range(4)] for _ in range(3)] for _ in range(2)]