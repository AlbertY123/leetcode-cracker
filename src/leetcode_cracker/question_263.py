def print_question():
    print("""An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.""")
def print_solution():

    print("""
class Solution:
    def isUgly(self, n: int) -> bool:
        number = n
        if n == 1:
            return True
        elif n<1 :
            return False
        else:
            while number%2 == 0:
                number = number/2
            if number == 1:
                return True
            while number%3 == 0:
                number = number/3
            if number == 1:
                return True
            while number%5 == 0:
                number = number/5
            if number == 1:
                return True
            
            

        
        
    """)
def solution_stats():
    print("""
        Time: Beats 5.76%
        Memory: Beats 44.19%
    """)
    

  
