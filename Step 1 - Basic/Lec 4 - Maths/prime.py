'''
────────────────────────────────────────────────────────────
📘 Question: Check for Prime Number
💡 Level: Easy
🎯 Task:
    You are given an integer `n`. 
    Check whether it is a prime number or not.

📖 Definition:
    A prime number has exactly two distinct divisors:
    1 and itself. It cannot be divided by any other number.

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 5
Output: True
🧾 Explanation:
    Divisors: 1, 5 → Only two divisors → ✔️ Prime

Input : n = 8
Output: False
🧾 Explanation:
    Divisors: 1, 2, 4, 8 → More than 2 divisors → ❌ Not Prime

────────────────────────────────────────────────────────────
🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def isPrime(self, n):
        #your code goes here
        ans = []
        for i in range(1,n+1):
            if n % i == 0:
                ans.append(i)
        return True if len(ans) == 2 else False


sol = Solution()
print(sol.isPrime(5))
print(sol.isPrime(42))