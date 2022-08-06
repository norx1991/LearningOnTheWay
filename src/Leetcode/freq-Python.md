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

bisect(list, val, low=0, high=len(list))

bisect_left(list, val)

insort(list, val)

insort_left(list, val)

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