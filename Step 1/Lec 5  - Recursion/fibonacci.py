'''
────────────────────────────────────────────────────────────
📘 Question: Fibonacci Number
💡 Level: Easy
🎯 Task:
    Given an integer `n`, return the nth Fibonacci number F(n).

📖 Fibonacci Sequence:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2), for n > 1

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 2
Output: 1
🧾 Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

Input : n = 3
Output: 2
🧾 Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

Input : n = 6
Output: 8
🧾 Explanation: 0 1 1 2 3 5 8 → 6th Fibonacci number is 8

────────────────────────────────────────────────────────────
🧠 Approach Variants:
    • Recursion (simple but slow: O(2^n))
    • Recursion with memoization (Top-down DP)
    • Iterative with 2 variables (Optimal: O(n) time, O(1) space)
    • Matrix exponentiation / Binet's Formula (Advanced: O(log n))

🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def fib(self, n: int) -> int:
        # 🛑 Base Case 1: F(0) = 0
        if n == 0:
            return 0
        # 🛑 Base Case 2: F(1) = 1
        elif n == 1:
            return 1
        # 🔁 Recursive Case: F(n) = F(n-1) + F(n-2)
        else:
            return self.fib(n - 1) + self.fib(n - 2)
