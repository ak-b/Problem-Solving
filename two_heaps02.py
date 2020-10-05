'''
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0

Time complexity #
The time complexity of our algorithm is O(N*K)O(N∗K) where ‘N’ is the total number of elements in the input array and ‘K’ is the size of the sliding window. This is due to the fact that we are going through all the ‘N’ numbers and, while doing so, we are doing two things:

Inserting/removing numbers from heaps of size ‘K’. This will take O(logK)O(logK)
Removing the element going out of the sliding window. This will take O(K)O(K) as we will be searching this element in an array of size ‘K’ (i.e., a heap).
Space complexity #
Ignoring the space needed for the output array, the space complexity will be O(K)O(K) because, at any time, we will be storing all the numbers within the sliding window.
'''
from heapq import *
import heapq


class SlidingWindowMedian:
  def __init__(self):
    self.maxHeap, self.minHeap = [], []

  def find_sliding_window_median(self, nums, k):
    result = [0.0 for x in range(len(nums) - k + 1)]
    for i in range(0, len(nums)):
      if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
        heappush(self.maxHeap, -nums[i])
      else:
        heappush(self.minHeap, nums[i])

      self.rebalance_heaps()

      if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
        # add the median to the the result array
        if len(self.maxHeap) == len(self.minHeap):
          # we have even number of elements, take the average of middle two elements
          result[i - k + 1] = -self.maxHeap[0] / \
                              2.0 + self.minHeap[0] / 2.0
        else:  # because max-heap will have one more element than the min-heap
          result[i - k + 1] = -self.maxHeap[0] / 1.0

        # remove the the element going out of the sliding window
        elementToBeRemoved = nums[i - k + 1]
        if elementToBeRemoved <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -elementToBeRemoved)
        else:
          self.remove(self.minHeap, elementToBeRemoved)

        self.rebalance_heaps()

    return result

  # removes an element from the heap keeping the heap property
  def remove(self, heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)

  def rebalance_heaps(self):
    # either both the heaps will have equal number of elements or max-heap will have
    # one more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()







