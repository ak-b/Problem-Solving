'''
Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and 
utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

Characteristics of Dynamic Programming #
Before moving on to understand different methods of solving a DP problem, let’s first take a look at what are the characteristics of a problem 
that tells us that we can apply DP to solve it.

1. Overlapping Subproblems #
Subproblems are smaller versions of the original problem. Any problem has overlapping sub-problems if finding its solution involves solving the same subproblem multiple times
2. Optimal Substructure Property #
Any problem has optimal substructure property if its overall optimal solution can be constructed from the optimal solutions of its subproblems.

DP offers two methods to solve a problem.

1. Top-down with Memoization #
In this approach, we try to solve the bigger problem by recursively finding the solution to smaller sub-problems.
Whenever we solve a sub-problem, we cache its result so that we don’t end up solving it repeatedly if it’s called multiple times. 
Instead, we can just return the saved result. This technique of storing the results of already solved subproblems is called Memoization.

'''
def calculateFibonacci(n):
  if n < 2:
    return n

  return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()




def calculateFibonacciRecur(memoize, n):
  if n < 2:
    return n

  # if we have already solved this subproblem, simply return the result from the cache
  if memoize[n] >= 0:
    return memoize[n]

  memoize[n] = calculateFibonacciRecur(
    memoize, n - 1) + calculateFibonacciRecur(memoize, n - 2)
  return memoize[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()

'''
2. Bottom-up with Tabulation #
Tabulation is the opposite of the top-down approach and avoids recursion. 
In this approach, we solve the problem “bottom-up” (i.e. by solving all the related sub-problems first). 
This is typically done by filling up an n-dimensional table. Based on the results in the table, the solution to the top/original problem is then computed.
Tabulation is the opposite of Memoization, as in Memoization we solve the problem and maintain a map of already solved sub-problems. 
In other words, in memoization, we do it top-down in the sense that we solve the top problem first (which typically recurses down to solve the sub-problems).
'''
def calculateFibonacci(n):
  memoize = [-1 for x in range(n+1)]
  return calculateFibonacciRecur(memoize, n)
def calculateFibonacci(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

  return dp[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
