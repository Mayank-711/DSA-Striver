'''
────────────────────────────────────────────────────────────
📘 Question: Print N to 1 using Recursion
💡 Level: Easy
🎯 Task:
    Given an integer `n`, print all numbers from `n` to `1` 
    using recursion only.

🚫 Constraints:
    ❌ Do not use any loops (for, while, etc.)
    ✅ Use recursion
    ✅ Each number must be printed on a new line

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 5
Output:
5
4
3
2
1

Input : n = 1
Output:
1

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def printnum(self,n):
        if n == 0:
            print(n)
        elif n == 1:
            print(n)
        else:
            print(n)
            return self.printnum(n-1)


sol = Solution()
sol.printnum(5)