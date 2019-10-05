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

## the divide and conquer paradigm

1. divide into smaller sub-problems
2. conquer via recursive calls
3. combine solutions of subproblem into the origin problem. 

## the count inversion problem 

### defination

Input: array A containing the numbers in some arbitrary order

Output: number of inversions, number of pairs (i,j) 

Example: (1,3,5,2,4,6)

Inversions:(3,2), (5,2), (5,4)

实际用途: 衡量具有相同数字不同顺序的列表的相似性 -> 相似推荐

### Hgh-level Approach
brute-force

two for loops

$O(n^2)$

a better method  ?

call an inversion (i,j) i<j:

|name| condition|
|----|-----------|
|left| i,j<n/2|
|right| i,j>n/2|
|split| i<n/2<j|

如果直接将数组进行二分递归查找inversions, 那么左边的数组找出来的是 left, 右边的数组找出来的是 right. 问题在于如何找出 split ? 

```python
def count_inversion(array, length):
    if n==1: return 0
    else:
        x = count_inversion(array[::length//2], n//2)
        y = count_inversion(array[length//2::], n//2)
        z = count_split(array,n)
        return x+y+z 
```
将merge_sort加入到其中. 原因: 首先, count_inversion 的时间复杂度和merge_sort的复杂度相似.那么在count_left 和count_right的过程中,我们可以**顺手**将左右数组排序.方便之后的count_split. 排序降低了整个数组的复杂度,同时没有影响count_split 的结果

当一个数组中没有split时, 可以想到, 左数组的数字都会比右数组的小.

在归并时,会直接先将左数组的数字copy到新数组中,再将右数组的数字copy到新数组末尾.

那么当有split的时候,如何计算呢? 

在归并的过程中,会有两个数组的比较,将小的数字放到新数组中.如果这个数字来自右数组,我们再看此时,左数组还有多少个未归并数字,就可以算出有多少个split, 以此累加.

即便新增了常数项的操作.$O(n)+O(n) = O(n)$


## matrix multiplication

assume X\*Y=Z  they are all N\*N

input_size : $O(n^2)$

running time of the straightforward iterative algorithm $O(n^3)$

first thing: divide 

divide into quadrant 
x= A B     Y = E F 
   C D         G H 

X\*Y = AE+BG  AF+BH
       CE+DG  CF+DH

### Recursive Algorithm 1 

step1 : recursively compute the  8 necessary products

step2 : do the necessary additions O(n^2)


Fact  :running time is $O(n^3)$

can we reduce the recursive calls 

### Strassen's Algorithm
step1: recursively compute only 7 products

step2: do the necessary clever addtions  still $O(n^2)$

Fact:  better than $O(n^3)$

the seven products : p1 = A(F-H) p2 = (A+B)H, P3 = (C+D)E P4= D(G-E)
P5=(A+D)(E+H), P6 =(B-D)(G+H) P7 = (A-C)(E+F)

### Closest pair (optional)

input: pairs in $R^2$

brute-force search:  take $O(n^2)$

1_D version 

1. sort points 
2. return closest points

2_D version 

依然采取分而治之的策略. 与归并排序相似.
1. 先根据x轴,y轴排序
2. 划分左右两组
3. 找到左组的最近对,和右组的最近对. 如果最近对恰巧在左组或右组,那么我们就找到了.this is a good case. 但也有可能一个在左组一个在右组. 如果是这种情形, 先将数据排序,按x轴计算出$x_\bar$, $\delta = min{distance_{right},distance_{left}$. 那么计算x轴在$x_\bar-\delta, x_\bar+\delta$这个区间内的点之间的距离.每个点只与和它近邻的7个点比较.按照这个方法,一定能在这个区间内找到. 
<img src="https://raw.githubusercontent.com/NickChilling/pic_bed/master/img/20191003142542.png"/>