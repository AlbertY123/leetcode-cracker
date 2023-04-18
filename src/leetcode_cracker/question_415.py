def print_question():
    print("""Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.""")
def print_solution():

    print("""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0:
            cur_i = int(num1[i]) if i >= 0 else 0
            cur_j = int(num2[j]) if j >= 0 else 0

            cur_sum = carry + cur_i + cur_j

            result.append(str(cur_sum%10))

            carry = cur_sum//10

            i = i-1
            j = j-1
        
        if carry:
            result.append(str(carry))

        return ''.join(reversed(result))
    """)
def solution_stats():
    print("""
        Time: Beats 20.1%
        Memory: Beats 9.1%
    """)
    

  
