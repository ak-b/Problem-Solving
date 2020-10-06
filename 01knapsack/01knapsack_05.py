'''
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

Example 1: #
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2: #
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

'''
'''
#Brute Force Solution
The time complexity of the above algorithm is exponential O(2^n)O(2
​n
​​ ), where ‘n’ represents the total number. The space complexity is O(n)O(n), this memory is used to store the recursion stack.
'''

def count_subsets(num, sum):
  return count_subsets_recursive(num, sum, 0)


def count_subsets_recursive(num, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1
  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # recursive call after selecting the number at the currentIndex
  # if the number at currentIndex exceeds the sum, we shouldn't process this
  sum1 = 0
  if num[currentIndex] <= sum:
    sum1 = count_subsets_recursive(
      num, sum - num[currentIndex], currentIndex + 1)

  # recursive call after excluding the number at the currentIndex
  sum2 = count_subsets_recursive(num, sum, currentIndex + 1)

  return sum1 + sum2


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()

#Top Down with Memoization
def count_subsets(num, sum):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(sum+1)] for y in range(len(num))]
  return count_subsets_recursive(dp, num, sum, 0)


def count_subsets_recursive(dp, num, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # check if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[currentIndex] <= sum:
      sum1 = count_subsets_recursive(
        dp, num, sum - num[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = count_subsets_recursive(dp, num, sum, currentIndex + 1)

    dp[currentIndex][sum] = sum1 + sum2

  return dp[currentIndex][sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()

'''
Bottom Up with Tabulation
 dp[index][sum] = dp[index-1][sum] + dp[index-1][sum-num[index]])
 time and space complexity of O(N*S)O(N∗S), where ‘N’ represents total numbers and ‘S’ is the desired sum.
'''
def count_subsets(num, sum):
  n = len(num)
  dp = [[-1 for x in range(sum+1)] for y in range(n)]

  # populate the sum = 0 columns, as we will always have an empty set for zero sum
  for i in range(0, n):
    dp[i][0] = 1

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for s in range(1, sum+1):
    dp[0][s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, sum+1):
      # exclude the number
      dp[i][s] = dp[i - 1][s]
      # include the number, if it does not exceed the sum
      if s >= num[i]:
        dp[i][s] += dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
