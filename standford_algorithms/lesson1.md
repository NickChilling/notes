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

