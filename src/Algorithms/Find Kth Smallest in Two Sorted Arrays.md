```C++
int findKthSmallest(int vec1[], int n1, int vec2[], int n2, int k) 
{ 
    if(n1 == 0)return vec2[k-1]; 
    else if(n2 == 0)return vec1[k-1]; 
    if(k == 1)return vec1[0] < vec2[0] ? vec1[0] : vec2[0]; 
     
    int idx1 = n1*1.0 / (n1 + n2) * (k - 1); 
    int idx2 = k - idx1 - 2; 
    if(vec1[idx1] == vec2[idx2]) 
        return vec1[idx1]; 
    else if(vec1[idx1] < vec2[idx2]) 
        return findKthSmallest(&vec1[idx1+1], n1-idx1-1, vec2, idx2+1, k-idx1-1); 
    else 
        return findKthSmallest(vec1, idx1+1, &vec2[idx2+1], n2-idx2-1, k-idx2-1); 
}
```