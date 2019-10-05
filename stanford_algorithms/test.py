# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # master method
# 
# a general tool to analyze divide and conquer algorithms.
# 
# ## motivation
# 当我们有了递归表达式之后,如何去计算时间复杂度?
#%% [markdown]
# 
# ## The Master Method
# 
# **Assumption:** 
# 1. all subproblems have equal size 
# 
# **Recurrence Format**
# 1. Base Case: T(n) <= a constant  for all sufficient small n 
# 2. For all larger n : T(n) <= aT(n/b)+O(n^d)  , where a = number of subproblems , b input size , d: exponent in suming time of combine step . a,b,d independent of n 
# 
# <img src="https://raw.githubusercontent.com/NickChilling/pic_bed/master/img/20191004095354.png"/>
#%% [markdown]
# ## examples
# 
# ### MergeSort
# a= 2 , b =2 , d = 1
# 
# $a=b^d$
# 
# $T(n)<=O(n^d\log n) = O(nlog)$
# 
# ### BinarySort
# 
# $T(n)<=T(n/2)+1$
# 
# a = 1 ,b = 2 , d= 0
# 
# $T(n) = n^0\log n$
# 
# ### integer multiplication
# $T(n) <= 4T(n/2)+n$
# 
# a = 4 b = 2  d= 1
# 
# $T(n) <= O^{\log_ba} =  O(n^2)$ 
# 
# Gauss's recursive
# 
# a = 3 b = 2  d = 1
# 
# $T(n) = O(n^{\log_23})$
# 
# ### Strassen's Matrix Multiplication Algorithm
# 
# a = 7 b= 2 c = 2
# 
# $T(n) = O(n^{\log_27})$
#%% [markdown]
# ## Proof
# Assume :
# 
# Recurrence is 
# 
# 1. T(1)<=c 
# 2. T(n) <= aT(n/b) +cn^d
# 
# and n is  a power of b. 
# 
# idea: generalize mergesort analysis
# 
# for each j = 0,1,2, $\log_bn$ , we have $a^j$ subproblems , each of size $n/b^j$
# 
# <img src="https://raw.githubusercontent.com/NickChilling/pic_bed/master/img/20191004112427.png"/>
# 
# <img src="https://raw.githubusercontent.com/NickChilling/pic_bed/master/img/20191004112512.png"/>
#%% [markdown]
# 对于在第i层的递归方程式, 我们有$a^j$ 个子问题, 规模为$n/b^j$, 那么归并这些问题,就需要 ${n/b^j}^d$ 也就得到上式

#%%



