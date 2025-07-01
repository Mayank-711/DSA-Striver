'''
────────────────────────────────────────────────────────────
📘 Question: If ElseIf
💡 Level: Easy
🎯 Task:
    Given marks of a student, print the grade based on:
    
    - Grade A if marks >= 90
    - Grade B if marks >= 70
    - Grade C if marks >= 50
    - Grade D if marks >= 35
    - Fail otherwise
────────────────────────────────────────────────────────────

📥 Input:
    marks = 95
📤 Output:
    Grade A
🧾 Explanation: marks are greater than or equal to 90.

📥 Input:
    marks = 14
📤 Output:
    Fail
🧾 Explanation: marks are less than 35.

🛠️ Use:
    For C++    : cout << variable_name;
    For Java   : System.out.print();
    For Python : print()
    For JS     : console.log()
────────────────────────────────────────────────────────────
'''
class Solution:
    def ifelse(self,marks):
        if marks >= 90:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 35:
            return "D"
        else:
            return 'Fail'

sol = Solution()
m = [91,71,51,37,14]
for i in m:
    print(sol.ifelse(i))