'''
────────────────────────────────────────────────────────────
📘 Question: Reverse an Array (In-Place)
💡 Level: Easy
🎯 Task:
    Given an array `arr` of size `n`, reverse the array **in-place**.

📌 In-Place means:
    ✅ Do not use extra space for another array.
    ✅ Swap elements using index manipulation.

────────────────────────────────────────────────────────────

📥 Examples:

Input : n = 5, arr = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Input : n = 6, arr = [1, 2, 1, 1, 5, 1]
Output: [1, 5, 1, 1, 2, 1]

Input : n = 3, arr = [1, 2, 1]
Output: [1, 2, 1]

────────────────────────────────────────────────────────────
🧠 Approach Ideas:
    • Two-pointer method (swap start and end).
    • Recursion (swap first & last, call on sub-array).
    • Use of Python slicing (not in-place ❌ for interviews).

🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def reverse_arr(self, arr, n):
        def rev(start,end):
            if start >= end:
                return
            arr[start],arr[end]=arr[end],arr[start]
            rev(start+1,end-1)
        rev(0,n-1)
        return arr





sol = Solution()
arr = [ 1,2,3,4,5,6]
n = len(arr)
print(sol.reverse_arr(arr,n))