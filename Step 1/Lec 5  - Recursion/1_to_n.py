'''
────────────────────────────────────────────────────────────
📘 Question: Print 1 to N using Recursion
💡 Level: Easy
🎯 Task:
    Given an integer `n`, write a function to print 
    all numbers from 1 to n using recursion only.

🚫 Constraints:
    ❌ No loops (for / while / do-while)
    ✅ Use recursion only
    ✅ Print each number on a new line in increasing order

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 5
Output:
1  
2  
3  
4  
5

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
    def printNumbers(self, n,current=1):
        # Your code goes here
        if current > n :
            return n
        print(current)
        self.printNumbers(n,current + 1)



sol = Solution()
sol.printNumbers(5)