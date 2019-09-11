# Introdution

## Integer Multiplication

before solving any problem, we need to define its input and output first.

in this problem

input: two n-digit numbers x and y

output: the product x,y

primitive operation: and or multiply 2 single-digit numbers

### algorithm in third grade

takes $O(n^2)$

### Karatsuba Multiplication

<img src="https://raw.githubusercontent.com/NickChilling/notes/master/pic_bed/20190906104616.png"/>

this is a Recursive Algorithm

<img src="https://raw.githubusercontent.com/NickChilling/notes/master/pic_bed/20190906104959.png"/>

<img src="https://raw.githubusercontent.com/NickChilling/notes/master/pic_bed/20190906105250.png"/>

这里巧妙的地方在于，如果直接按照公式进行递归调用。需要四次递归计算 $a*c$,$b*d$,$a*d$,$b*c$。通过计算$(a+b)*(c+d)-ac-bd$减少了一次递归计算。

## Divide & Conquer: Merge sort

Divide $ Conquer: break down a problem into smaller sub problems which you then solve recursively, and combine these results.

Input: array of n numbers, unsorted

Output: same numbers sorted

### Pseudocode

- recursively sort 1st half / 2nd 
- merge into one
ignore base cases: n = 0 or 1

### implementation

```python
def merge_sort(array):
    n = len(array)
    if len(array)<=1 :
        return
    front = merge_sort(array[:n])
    end =merge_sort(array[n:])
    return merge(front, end)

def merge(arr1, arr2):
    m = len(arr1)+len(arr2)
    result = []
    i = 0
    j = 0
    for idx in range(m):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
```

## Analysis

T(n) is big-Oh of f(n)  -> bounded above by constant multiple of f(n)
the worst-case running time of an algorithm

Formal Defination

$T(n)=O(f(n))$
if and only if there exist constants, $c>0$ ，so that $T(n) <= c*f(n)$

big_O: greater_than to f(n);
omega: less_than to f(n);
theta: equals to f(n);

little_O: for every c, $T(n) <=c*f(n)$
