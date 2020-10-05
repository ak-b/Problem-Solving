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
#Quicksort
import random


def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivotIndex = random.randint(low, high)
  nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

#Median of Medians
def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  median = median_of_medians(nums, low, high)
  # find the median in the array and swap it with 'nums[high]' which will become our pivot
  for i in range(low, high):
    if nums[i] == median:
      nums[i], nums[high] = nums[high], nums[i]
      break

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def median_of_medians(nums, low, high):
  n = high - low + 1
  # if we have less than 5 elements, ignore the partitioning algorithm
  if n < 5:
    return nums[low]

  # partition the given array into chunks of 5 elements
  partitions = [nums[j:j+5] for j in range(low, high+1, 5)]

  # for simplicity, lets ignore any partition with less than 5 elements
  fullPartitions = [
    partition for partition in partitions if len(partition) == 5]

  # sort all partitions
  sortedPartitions = [sorted(partition) for partition in fullPartitions]

  # find median of all partations; the median of each partition is at index '2'
  medians = [partition[2] for partition in sortedPartitions]

  return partition(medians, 0, len(medians)-1)


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
