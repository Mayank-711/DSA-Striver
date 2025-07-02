'''
────────────────────────────────────────────────────────────
📘 Question: Palindrome Number
💡 Level: Easy
🎯 Task:
    You are given an integer `n`. 
    Check whether the number is a palindrome.

    A palindrome number is one that reads the same 
    both left-to-right and right-to-left.

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 121
Output: True
🧾 Explanation:
    Left to right: 121
    Right to left: 121 (same)

Input : n = 123
Output: False
🧾 Explanation:
    Left to right: 123
    Right to left: 321 (not same)

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        