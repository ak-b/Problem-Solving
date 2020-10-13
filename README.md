# Problem-Solving
This repo is to serve as a guide to common problem solving patterns using various algorithms.Each pattern will be a complete tool - consisting of data structures, algorithms, and analysis techniques - to solve a specific category of problems. The goal is to build an understanding of the underlying pattern so that we can apply that pattern to solve other problems

# Patterns:

1. **Sliding Window**
In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size.In some problems, the size of the sliding window is not fixed. We have to expand or shrink the window based on the problem constraints. We will see a few examples of such problems in the next chapters.
>eg: Given an array, find the average of all contiguous subarrays of size ‘K’ in it
2. **Two Pointers**
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray.
>eg: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target
3. **Fast& Slow Pointers**
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.
>eg: Finding a cycle in a LinkedList
4. **Merge Intervals**
This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other:
>eg: Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other
5. **Cyclc Sort**
This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range.
>eg: You are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers
6. **In-place reversal of a Linked List**
Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem
>eg: Using the existing node objects and without using extra memory
7. **Tree Breadth First Search**
Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be O(W)O(W), where ‘W’ is the maximum number of nodes on any level.
>eg: Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level
8. **Tree Depth First Search**
This pattern is based on the Depth First Search (DFS) technique to traverse a tree.We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. This also means that the space complexity of the algorithm will be O(H)O(H), where ‘H’ is the maximum height of the tree.
>eg: Tree traversal using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. 
9. **Two Heaps**
In many problems, where we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern is an efficient approach to solve such problems.This pattern uses two Heaps to solve these problems; A Min Heap to find the smallest element and a Max Heap to find the biggest element.
>eg: In many problems, where we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern is an efficient approach to solve such problems.This pattern uses two Heaps to solve these problems; A Min Heap to find the smallest element and a Max Heap to find the biggest element.
10. **Subsets**
A huge number of coding interview problems involve dealing with Permutations and Combinations of a given set of elements. This pattern describes an efficient Breadth First Search (BFS) approach to handle all these problems.
>eg: Problems involve dealing with Permutations and Combinations of a given set of elements
11. **Modified Binary Search**
As we know, whenever we are given a sorted Array or LinkedList or Matrix, and we are asked to find a certain element, the best algorithm we can use is the Binary Search.This pattern describes an efficient way to handle all problems involving Binary Search
>eg: Pattern describes an efficient way to handle all problems involving Binary Search.
12. **Bitwise XOR**
XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise. In other words, it only returns 1 if exactly one bit is set to 1 out of the two bits in comparison
>eg: Given an array of n-1n−1 integers in the range from 11 to nn, find the one number that is missing from the array.
13. **Top 'K' Elements**
Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.The best data structure that comes to mind to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements.
>eg: To find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.
14. **K-way Merge**
This pattern helps us solve problems that involve a list of sorted arrays.Whenever we are given ‘K’ sorted arrays, we can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays. We can push the smallest (first) element of each sorted array in a Min Heap to get the overall minimum. While inserting elements to the Min Heap we keep track of which array the element came from. We can, then, remove the top element from the heap to get the smallest element and push the next element from the same array, to which this smallest element belonged, to the heap. We can repeat this process to make a sorted traversal of all elements.
>eg: For list of sorted arrays, whenever we are given ‘K’ sorted arrays, we can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays. 
15. **0/1 Knapsack Problem (Dynamic programming)**
0/1 Knapsack pattern is based on the famous problem with the same name which is efficiently solved using Dynamic Programming (DP).In this pattern, we will go through a set of problems to develop an understanding of DP. We will always start with a brute-force recursive solution to see the overlapping subproblems, i.e., realizing that we are solving the same problems repeatedly.After the recursive solution, we will modify our algorithm to apply advanced techniques of Memoization and Bottom-Up Dynamic Programming to develop a complete understanding of this pattern.
>eg: Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit out of the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.
16. **Topological Sort(Graph)**
Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.This pattern defines an easy way to understand the technique for performing topological sorting of a set of elements and then solves a few problems using it.
>eg: To find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.




