'''
────────────────────────────────────────────────────────────
📘 Question: Count all Digits of a Number
💡 Level: Easy
🎯 Task:
    Given an integer `n`, return the total number of digits 
    in the number.

    No leading zeroes will be present, except for `n = 0`.

────────────────────────────────────────────────────────────

📥 Input:
    n = 4
📤 Output:
    1
🧾 Explanation: Only one digit in 4

📥 Input:
    n = 14
📤 Output:
    2
🧾 Explanation: There are two digits in 14

🛠️ Use:
    For C++    : cout << variable_name;
    For Java   : System.out.print();
    For Python : print()
    For JS     : console.log()
────────────────────────────────────────────────────────────
'''


class Solution:
    def countdigit(self,n):
        return len(str(n))


sol = Solution()
ar = [ 1,214,14,4532]
for x in ar:
    print(sol.countdigit(x))