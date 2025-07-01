'''
────────────────────────────────────────────────────────────
📘 Question: printNumber
💡 Level: Easy
🎯 Task: Complete the function `printNumber` which takes an 
         integer input from the user and prints it on the screen.
────────────────────────────────────────────────────────────

📥 Input (User gives value):
    7
📤 Output:
    7

📥 Input:
    -5
📤 Output:
    -5

🛠️ Use:
    For C++    : cout << variable_name;
    For Java   : System.out.print();
    For Python : print()
    For JS     : console.log()
────────────────────────────────────────────────────────────
'''

class Solution:
    def printNumber(self):
        n = int(input())
        print(n)


sol = Solution()
sol.printNumber()