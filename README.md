# Problem-Solving
This repo is to serve as a guide to common problem solving patterns using various algorithms.Each pattern will be a complete tool - consisting of data structures, algorithms, and analysis techniques - to solve a specific category of problems. The goal is to build an understanding of the underlying pattern so that we can apply that pattern to solve other problems

# Patterns:

1. **Sliding Window**
>eg: Given an array, find the average of all contiguous subarrays of size ‘K’ in it
2. **Two Pointers**
>eg: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target
3. **Fast& Slow Pointers**
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.
>eg: Finding a cycle in a LinkedList
4. **Merge Intervals**
This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other:
>eg: Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other
5. **Cyclc Sort**
>eg: You are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers
6. **In-place reversal of a Linked List**
>eg: Using the existing node objects and without using extra memory
7. **Tree Breadth First Search**
>eg: Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level
8. **Tree Depth First Search**
>eg: Tree traversal using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. 
9. **Two Heaps**
>eg: In many problems, where we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern is an efficient approach to solve such problems.This pattern uses two Heaps to solve these problems; A Min Heap to find the smallest element and a Max Heap to find the biggest element.
10. **Subsets**
>eg: Problems involve dealing with Permutations and Combinations of a given set of elements
11. **Modifief Binary Search**
>eg: Pattern describes an efficient way to handle all problems involving Binary Search.
12. **Bitwise XOR**
>eg: Given an array of n-1n−1 integers in the range from 11 to nn, find the one number that is missing from the array.
13. **Top 'K' Elements**
>eg: To find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.
14. **K-way Merge**
>eg: For list of sorted arrays, whenever we are given ‘K’ sorted arrays, we can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays. 
15. **0/1 Knapsack Problem (Dynamic programming)**
>eg: Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit out of the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.
16. **Topological Sort(Graph)**
>eg: To find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.




