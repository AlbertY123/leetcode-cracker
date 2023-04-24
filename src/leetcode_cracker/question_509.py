def print_question():
    print("""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
""")
def print_solution():

    print("""
class Solution:
    def fib(self, n: int) -> int:
        oldfib = 1
        currentfib = 3
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(n):
            oldfib = oldfib + currentfib
            currentfib = currentfib-oldfib
        return currentfib



    """)
def solution_stats():
    print("""
        Time: Beats 5.40%
        Memory: Beats 90.66%
    """)
    

  
