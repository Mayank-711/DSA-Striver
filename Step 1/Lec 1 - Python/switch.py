'''
────────────────────────────────────────────────────────────
📘 Question: Switch Case
💡 Level: Easy
🎯 Task:
    Given an integer `day` denoting the day number (1 to 7),
    print the name of the weekday.

    Week starts from Monday (1) to Sunday (7).
    For values < 1 or > 7, print "Invalid".

    Output must have only the 1st letter capitalised.
────────────────────────────────────────────────────────────

📥 Input:
    day = 3
📤 Output:
    Wednesday

📥 Input:
    day = 8
📤 Output:
    Invalid

🛠️ Use:
    For C++    : cout << variable_name;
    For Java   : System.out.print();
    For Python : print()
    For JS     : console.log()
────────────────────────────────────────────────────────────
'''
class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                return "Mon"
            case 2:
                return "Tue"
            case 3:
                return "Wed"
            case 4:
                return "Thur"
            case 5:
                return "Fri"
            case 6:
                return "Sat"
            case 7:
                return "Sun"
            case _:
                return "Invalid"


sol = Solution()
d = [1,2,3,4,5,6,7,8]
for i in d:
    print(sol.whichWeekDay(i))