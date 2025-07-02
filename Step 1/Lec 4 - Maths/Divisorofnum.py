'''
────────────────────────────────────────────────────────────
📘 Question: Divisors of a Number
💡 Level: Easy
🎯 Task:
    Given an integer `n`, return all its divisors 
    in a sorted list.

📖 Definition:
    A divisor of `n` is a number that divides `n` completely 
    without leaving any remainder.

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 6
Output: [1, 2, 3, 6]
🧾 Explanation:
    All numbers that divide 6 → 6 % i == 0:
    → 1, 2, 3, 6

Input : n = 8
Output: [1, 2, 4, 8]
🧾 Explanation:
    All numbers that divide 8 → 8 % i == 0:
    → 1, 2, 4, 8

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def divisors(self, n):
        ans = []
        for i in range(1,n+1):
            if n % i == 0:
                ans.append(i)
        return ans



sol = Solution()
print(sol.divisors(42))