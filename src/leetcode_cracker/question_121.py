def print_question():
    print("""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.""")
def print_solution():

    print("""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Init variables
        minvalue = prices[0] 
        maxvalue = 0 

        for i in range(len(prices)):
            #Checking for lowest price
            if prices[i]<minvalue: 
                minvalue = prices[i]

            #Check for higher profit
            elif prices[i]-minvalue > maxvalue: 
                maxvalue = prices[i]-minvalue
        #Return Highest Profit
        return maxvalue
    """)
def solution_stats():
    print("""
        Time: Beats 80.74%
        Memory: Beats 80.8%
    """)
    

  
