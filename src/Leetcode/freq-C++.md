# list
- front()
- back()
- push_front()
- pop_front()
- push_back()
- pop_back()
- insert(iter, val)
- insert(iter, n, val)
- erase()
- remove()
- unique()
- merge()
- splice(position, list& x)
- splice(position, list& x, first, last)

# vector
- front()
- back()
- push_back()
- pop_back()
- insert()
- erase()
- emplace(pos, args)
- assign()
- resize()
- shrink_to_fit()


# string
- push_back(char)
- pop_back()
- copy(char*, len, pos)
- find()
- rfind()
- substr(pos, len)
- compare(str)
- npos: maximum value for size_t

# unordered_map
- find()
- count()
- insert()
- erase(iter)
- erase(key_type)

# priority_queue
- ```
  std::priority_queue<int, std::vector<int>, std::greater<int>> (minheap)
  std::priority_queue<int> (minheap) (maxheap)
  ```
- push(val)
- pop()
- top()
- size()
- empty()
- emplace()

# set
- insert()
- erase(iter)
- erase(val)
- find()
- count()
- lower_bound()
- upper_bound()

# deque
- front()
- back()
- push_back()
- push_front()
- pop_back()
- pop_front()
- insert()
- erase()

# queue
- front()
- back()
- push()
- pop()
- emplace()

# stack
- top()
- push()
- pop()
- emplace()

# Lambda

  `[]() {}`

- [&x]: capture x by ref
- [&]: capture all by ref
- [=]: capture all by value
- [&, x]: x by value, others by ref

# Syntax

auto data = std::make_unique<unsigned char[]>(16000);

```c++
int *p1 = malloc(4*sizeof(int))
memcpy (str1, str2, sizeof(str2))
char *pBuffer = new char[1024]
delete[] pBuffer
```

```c++
// A 3x4 2D vector of integers, all initialized to 0
std::vector<std::vector<int>> matrix(nrows, std::vector<int>(ncols, 0));
```

# Algorithms
- swap(T& a, T& b)
- max(T& a, T& b)
- min(T& a, T& b)
- max_element()
- min_element()
- sort()
- partial_sort()
- stable_sort()
- all_of()
- any_of()
- none_of()
- for_each()
- count()
- count_if()
- find()
- find_if()
- find_if_not()
- find_end()
- search()
- copy()
- copy_n()
- fill()
- transform()
- iota()
- accumulate()
- remove()
- remove_if()
- replace()
- replace_if()
- reverse()
- reverse_copy()
- rotate()
- unique()
- random_shuffle()
- partition()
- lower_bound()
- upper_bound()
- merge()
- includes()
- set_difference()
- set_intersection()
- set_symmetric_difference()
- set_union()
- is_heap()
- make_heap()
- push_heap()
- pop_heap()
- sort_heap()
- is_permutation()
- next_permutation()
- prev_permutation()
- partial_sum()
- adjacent_difference()
- exclusive_scan()
- inner_product()
- lexicographical_compare()

  

