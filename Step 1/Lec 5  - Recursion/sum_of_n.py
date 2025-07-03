'''
────────────────────────────────────────────────────────────
📘 Question: Sum of First N Numbers (Using Recursion)
💡 Level: Easy
🎯 Task:
    Given an integer N, return the sum of the first N 
    natural numbers using recursion only.

🧠 Formula (Not Allowed in This Task):
    sum = N * (N + 1) // 2 — ❌ Not allowed, must use recursion

────────────────────────────────────────────────────────────

📥 Examples:

Input : N = 4
Output: 10
🧾 Explanation:
    1 + 2 + 3 + 4 = 10

Input : N = 2
Output: 3
🧾 Explanation:
    1 + 2 = 3

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def NnumbersSum(self,n):
        #your code goes here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return n + self.NnumbersSum(n-1)


sol = Solution()
print(sol.NnumbersSum(5))