'''
────────────────────────────────────────────────────────────
📘 Question: Reverse Digits of a Number
💡 Level: Easy
🎯 Task:
    You are given an integer `n`. 
    Return the integer formed by placing the digits of `n`
    in reverse order.

────────────────────────────────────────────────────────────

📥 Input:
    n = 25
📤 Output:
    52
🧾 Explanation: Reverse of 25 is 52

📥 Input:
    n = 123
📤 Output:
    321
🧾 Explanation: Reverse of 123 is 321

🛠️ Use:
    For C++    : cout << variable_name;
    For Java   : System.out.print();
    For Python : print()
    For JS     : console.log()
────────────────────────────────────────────────────────────
'''

class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Convert the absolute value of x to string and reverse it
        rev = int(str(abs(x))[::-1])

        # Step 2: Check for 32-bit signed integer overflow
        # If reversed number exceeds 2^31 - 1, return 0 (invalid)
        if rev > 2**31 - 1:
            return 0

        # Step 3: Return the reversed number with correct sign
        # If original x was negative, make rev negative
        return rev if x >= 0 else -rev
