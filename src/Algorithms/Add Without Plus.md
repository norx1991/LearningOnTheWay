```c++
int add_no_arithm(int a, int b) { 
    if (b == 0) return a; 
    int sum = a ^ b; // add without carrying 
    int carry = (a & b) << 1; // carry, but don’t add 
    return add_no_arithm(sum, carry); // recurse 
  }
```