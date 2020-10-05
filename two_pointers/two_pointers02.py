'''
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

Time Complexity #
The time complexity of the above algorithm will be O(N)O(N), where ‘N’ is the total number of elements in the given array.

Space Complexity #
The algorithm runs in constant space O(1)O(1).

'''
def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate


def remove_element(arr, key):
  nextElement = 0  # index of the next element which is not 'key'
  for i in range(len(arr)):
    if arr[i] != key:
      arr[nextElement] = arr[i]
      nextElement += 1

  return nextElement


def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))


main()


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
'''
Time and Space Complexity: The time complexity of the above algorithm will be O(N)O(N), where ‘N’ is the total number of elements in the given array.

The algorithm runs in constant space O(1)O(1).
'''
