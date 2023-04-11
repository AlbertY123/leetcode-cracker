def print_question():
    print("""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

            A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """)
def print_solution():

    print("""
   class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        # Init Both Variables
        i = 0
        j = 0

        # Loop Through Both Variables
        while i<len(s) and j<len(t):
            # If both Pointers are the same, increment both by one
            if s[i] == t[j]:
                i += 1
                j += 1
            #Otherwise, only increment the second pointer
            else:
                j += 1
        #If the function has finnished running, return true.
        if i == len(s):
            return True
        else:
            return False
    """)
def solution_stats():
    print("""
        Time: Beats 30.59%
        Memory: Beats 30.17%
    """)
    

  
