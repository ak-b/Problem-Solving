'''
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
The only trick is that we can have negative numbers in the input array, which will make it a bit difficult to generate the output array with squares in sorted order.

Time complexity #
The time complexity of the above algorithm will be O(N)O(N) as we are iterating the input array only once.

Space complexity #
The space complexity of the above algorithm will also be O(N)O(N); this space will be used for the output array
'''
def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
