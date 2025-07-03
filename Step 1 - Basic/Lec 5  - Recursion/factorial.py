'''
────────────────────────────────────────────────────────────
📘 Question: Factorial of a Number using Recursion
💡 Level: Easy
🎯 Task:
    Given an integer `n`, return its factorial using recursion.

📖 Definition:
    Factorial of `n` (denoted as n!) is the product of 
    all positive integers less than or equal to `n`.

    Example:
    5! = 5 × 4 × 3 × 2 × 1 = 120

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 5
Output: 120
🧾 Explanation:
    5 × 4 × 3 × 2 × 1 = 120

Input : n = 3
Output: 6
🧾 Explanation:
    3 × 2 × 1 = 6

────────────────────────────────────────────────────────────
📌 Constraints:
    • n ≥ 0
    • Factorial of 0 is 1 (0! = 1)

🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def Factorial(self,n):
        #your code goes here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return n * self.Factorial(n-1)


sol = Solution()
print(sol.Factorial(5))