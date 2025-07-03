'''
────────────────────────────────────────────────────────────
📘 Question: Check if String is Palindrome
💡 Level: Easy
🎯 Task:
    Given a string `s`, return True if the string is a palindrome,
    otherwise return False.

📖 Definition:
    A string is a palindrome if it reads the same forward and backward.

────────────────────────────────────────────────────────────

📥 Examples:

Input : s = "hannah"
Output: True
🧾 Explanation: Reverse of "hannah" is "hannah" → same as original.

Input : s = "aabbaaa"
Output: False
🧾 Explanation: Reverse of "aabbaaa" is "aaabbaa" → not the same.

────────────────────────────────────────────────────────────
🧠 Constraints:
    • Case-sensitive comparison (e.g., "Aa" is not equal to "aa")
    • No spaces, but can be extended to ignore spaces and punctuation.

🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 🔹 Step 1: Remove all non-alphanumeric characters and convert to lowercase
        # Example: "A man, a plan, a canal: Panama" → "amanaplanacanalpanama"
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # 🔹 Step 2: Check if the cleaned string is equal to its reverse
        return s == s[::-1]
