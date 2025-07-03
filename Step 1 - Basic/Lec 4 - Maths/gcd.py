'''
────────────────────────────────────────────────────────────
📘 Question: GCD of Two Numbers
💡 Level: Easy
🎯 Task:
    Given two integers `n1` and `n2`, return their 
    Greatest Common Divisor (GCD).

📖 Definition:
    The Greatest Common Divisor (GCD) of two integers is 
    the largest positive integer that divides both numbers 
    exactly (without remainder).

────────────────────────────────────────────────────────────

📥 Examples:

Input : n1 = 4, n2 = 6
Output: 2
🧾 Explanation:
    Divisors of 4: 1, 2, 4  
    Divisors of 6: 1, 2, 3, 6  
    Common: 1, 2 → GCD = 2

Input : n1 = 9, n2 = 8
Output: 1
🧾 Explanation:
    Divisors of 9: 1, 3, 9  
    Divisors of 8: 1, 2, 4, 8  
    Common: 1 → GCD = 1

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
import math
class Solution:
    def GCD(self, n1, n2):
        return math.gcd(n1,n2)


sol = Solution()
print(sol.GCD(18,12))