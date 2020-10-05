'''
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9
Time Complexity: Time complexity of this solution is O(n)O(n) as we iterate through all numbers of the input once.

Space Complexity: The algorithm runs in constant space O(1).


'''
def find_single_number(arr):
  num = 0
  for i in arr:
      num ^= i
  return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()
