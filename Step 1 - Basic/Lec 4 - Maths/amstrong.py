'''
────────────────────────────────────────────────────────────
📘 Question: Check if the Number is Armstrong
💡 Level: Easy
🎯 Task:
    You are given an integer `n`.
    Check whether it is an Armstrong number or not.

📖 Definition:
    An Armstrong number is a number that is equal to the 
    sum of its own digits each raised to the power of 
    the number of digits.

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 153
Output: True
🧾 Explanation:
    Number of digits = 3
    1³ + 5³ + 3³ = 1 + 125 + 27 = 153 → ✔️ Armstrong

Input : n = 12
Output: False
🧾 Explanation:
    Number of digits = 2
    1² + 2² = 1 + 4 = 5 → ❌ Not Armstrong

Input : n = 370
Output: True

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''

class Solution:
    def amstrong(self,n):
        power = len(str(n))
        digits = str(n)
        ans = 0
        for i in range(len(digits)):
            ans += int(digits[i])**power
        return n == ans



sol = Solution()
print(sol.amstrong(153))
print(sol.amstrong(226))