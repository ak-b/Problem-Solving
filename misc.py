'''
Given an unsorted array of numbers, find Kth smallest number in it.Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three smaller numbers are
[1, 2, 5].

Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

Solve using:

1. Brute-force

2. Brute-force using Sorting

3. Using Max-Heap

4. Using Min-Heap

5. Using Partition Scheme of Quicksort

6. Using Randomized Partitioning Scheme of Quicksort

7. Using the Median of Medians

Solution:
Theoretically, the Median of Medians algorithm gives the best time complexity of O(N)O(N) but practically both the Median of Medians and 
the Randomized Partitioning algorithms nearly perform equally.In the context of Quicksort, given an O(N)O(N) selection algorithm using the 
Median of Medians, one can use it to find the ideal pivot (the median) at every step of quicksort and thus produce a sorting algorithm with 
O(NlogN)O(NlogN) running time in the worst-case. 

'''
