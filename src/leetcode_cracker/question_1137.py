def print_question():
    print("""The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.""")
def print_solution():

    print("""
class Solution:
    def tribonacci(self, n: int) -> int:
        answer = [0, 1, 1]

        for i in range(n):
            answer.append(answer[i]+answer[i+1]+answer[i+2])
        return answer[n]


    """)
def solution_stats():
    print("""
        Time: Beats 70.12%
        Memory: Beats 93.25%
    """)
    

  
